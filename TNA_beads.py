## Test protocolo only using 8 samples. 

## VOLUMEN De Muestra: 50 µL
## VOLUMEN de Elusion: 50 µL

def get_values(*names):
    import json
    _all_values = json.loads("""{"mag_mod":"magnetic module gen2", "pipette_type":"p300_multi_gen2","pipette_mount":"left","sample_number":16,"sample_volume":50,"bead_ratio":1,"elution_buffer_volume":50,"incubation_time":5,"settling_time":5,"drying_time":5}""")
    return [_all_values[n] for n in names]


import math


metadata = {
    'protocolName': 'TBA Purification',
    'author': 'Bernardo Pollak <bpollak@meristem.bio>',
    'source': 'Protocol Library',
    'apiLevel': '2.4'
    }


def run(protocol_context):

    [mag_mod, pipette_type, pipette_mount, sample_number, sample_volume,
     bead_ratio, elution_buffer_volume, incubation_time, settling_time,
     drying_time] = get_values(  # noqa: F821
        "mag_mod", "pipette_type", "pipette_mount", "sample_number",
        "sample_volume", "bead_ratio", "elution_buffer_volume",
        "incubation_time", "settling_time", "drying_time"
    )

    ## Modules
    mag_deck = protocol_context.load_module(mag_mod, '1')
    mag_plate = mag_deck.load_labware('biorad_96_wellplate_200ul_pcr')
    
    
    ## Labware
    output_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '2', 'output plate')
    # Number (and position) of tipracks
    total_tips = sample_number*8
    tiprack_num = math.ceil(total_tips/96)
    slots = ['3', '6', '7', '8', '9', '10', '11'][:tiprack_num]

    
    ## Instruments
    # Pipette selection
    pip_range = pipette_type.split('_')[0]
    if pip_range == 'p1000':
        tip_name = 'opentrons_96_tiprack_1000ul'
    elif pip_range == 'p300' or pip_range == 'p50':
        tip_name = 'opentrons_96_tiprack_300ul'
    elif pip_range == 'p20':
        tip_name = 'opentrons_96_tiprack_20ul'
    else:
        tip_name = 'opentrons_96_tiprack_10ul'
    tipracks = [protocol_context.load_labware(tip_name, slot) for slot in slots]

    # Pipette load
    pipette = protocol_context.load_instrument(pipette_type, pipette_mount, tip_racks=tipracks)

    mode = pipette_type.split('_')[1]

    
    ## Labware
    # Defining containers for reagents depending on the total number of samples
    if mode == 'single':
        if sample_number <= 5:
            reagent_container = protocol_context.load_labware(
                'opentrons_24_tuberack_nest_2ml_snapcap', '4')
            liquid_waste = protocol_context.load_labware(
                'nest_12_reservoir_15ml', '5').wells()[-1]
        else:
            reagent_container = protocol_context.load_labware(
                'nest_12_reservoir_15ml', '4')
            liquid_waste = reagent_container.wells()[-1]
        samples = [well for well in mag_plate.wells()[:sample_number]]
        output = [well for well in output_plate.wells()[:sample_number]]
    else:
        reagent_container = protocol_context.load_labware(
            'nest_12_reservoir_15ml', '4')
        liquid_waste = reagent_container.wells()[-1]
        col_num = math.ceil(sample_number/8)
        samples = [col for col in mag_plate.rows()[0][:col_num]]
        output = [col for col in output_plate.rows()[0][:col_num]]

        
    ## Labware 
    # Define the internal structure of the reagents containers
    beads = reagent_container.wells()[0]
    ethanol = reagent_container.wells()[1]
    ethanol_salt = reagent_container.wells()[2]
    elution_buffer = reagent_container.wells()[3]

    
    # Define bead and mix volume
    bead_volume = sample_volume * bead_ratio

    if bead_volume < 30:
        bead_volume = 30

    mix_vol = 30
    total_vol = bead_volume + sample_volume + 5

    if (bead_volume > pipette.max_volume) or (mix_vol > pipette.max_volume) or (total_vol > pipette.max_volume):
    	print ("Some volume is higher than max pipette volume ")
    	quit()

        
    ## Defining default values for pipetting behavior 
    # Mix beads and PCR samples
    pipette.flow_rate.aspirate = 25
    pipette.flow_rate.dispense = 300
    pipette.well_bottom_clearance.aspirate = 2
    pipette.well_bottom_clearance.dispense = 5
    air_vol = pipette.max_volume * 0.1

    
	## Start protocol:
    # Mix beads and dispense to sample
    for target in samples:
        pipette.pick_up_tip()
        pipette.mix(10, 50, beads)
        pipette.transfer(bead_volume, beads, target, new_tip='never')
        pipette.mix(20, 50, target)
        pipette.blow_out(liquid_waste)
        pipette.drop_tip()

    # Incubate beads and PCR product at RT for 5 minutes
    protocol_context.delay(minutes=incubation_time)

    # Engagae MagDeck and incubate
    mag_deck.engage(height=10)
    protocol_context.delay(minutes=settling_time)

    # Remove supernatant from magnetic beads 
    pipette.flow_rate.aspirate = 10
    pipette.flow_rate.dispense = 150

    for target in samples:
        pipette.transfer(total_vol, target, liquid_waste.top(), air_gap=air_vol, blow_out=True)

    # Wash beads once with 70% ethanol 0.5M NaCl
    pipette.flow_rate.aspirate = 25

    # Try using same tip for all
    #### Maybe at this point do mixing per tip usage......
    mag_deck.disengage()
    for target in samples:
        pipette.pick_up_tip()
        pipette.transfer(150, ethanol_salt, target.top(), air_gap=air_vol, new_tip='never')
        pipette.mix(10, 75, target)
        pipette.drop_tip()

    mag_deck.engage(height=10)
    protocol_context.delay(minutes=5)

    # Remove 80% ethanol ## changed tips
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(150, target, liquid_waste.top(), air_gap=air_vol, new_tip='never')
    pipette.drop_tip()

    # Second wash
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(150, ethanol, target.top(), air_gap=air_vol, new_tip='never')

    protocol_context.delay(minutes=1)

    # Remove 80% ethanol ## changed tips
    for target in samples:
        pipette.transfer(150, target, liquid_waste.top(), air_gap=air_vol, new_tip='never')
    pipette.drop_tip()
    
    # Wash beads third time #
    # Try using same tip for all
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(150, ethanol, target.top(), air_gap=air_vol, new_tip='never')
    
    protocol_context.delay(minutes=1)
    # And carefully remove 80% ethanol
    ### I see ethanol sticking and falling on tip and on plate / reduce air volume?
    pipette.flow_rate.aspirate = 15
    pipette.well_bottom_clearance.aspirate = 1
    for target in samples:
        pipette.transfer(160, target, liquid_waste.top(), air_gap=air_vol, new_tip='never')
        pipette.blow_out()
        pipette.transfer(30, target, liquid_waste.top(), air_gap=air_vol, new_tip='never')
        pipette.blow_out()

    pipette.drop_tip()

    # Dry at RT
    protocol_context.delay(minutes=drying_time)

    # Disengage MagDeck
    mag_deck.disengage()

    # Elution with stronger mixing
    pipette.flow_rate.aspirate = 50
    pipette.flow_rate.dispense = 300
    for target in samples:
        pipette.pick_up_tip()
        pipette.transfer(
            elution_buffer_volume+5, elution_buffer, target, new_tip='never')
        pipette.mix(20, mix_vol, target)
        pipette.drop_tip()

    # Incubate at RT
    protocol_context.delay(minutes=5)

    # Engage MagDeck and remain engaged for DNA elution
    mag_deck.engage(height=10)
    protocol_context.delay(minutes=settling_time)

    # Transfer clean PCR product to a new well
    pipette.flow_rate.aspirate = 10
    for target, dest in zip(samples, output):
        pipette.transfer(elution_buffer_volume, target, dest, blow_out=True)