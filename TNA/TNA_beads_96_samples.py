## Test this protocolo using only 8 samples. 

## VOLUMEN De Muestra: 50 µL
## VOLUMEN de Elusion: 50 µL

# \ Comentarios de Bernardo
# || Comentarios de Benjamín

import math
import json

def get_values(*names):
    # Here you must change the values to meet your needs 
    _all_values = json.loads("""{"mag_mod":"magnetic module gen2", "pipette_type":"p300_multi_gen2","pipette_mount":"right","sample_number":96,"sample_volume":50,"bead_ratio":1,"elution_buffer_volume":50,"incubation_time":15,"settling_time":7,"drying_time":5,"custom_tiprack":"yes"}""")
    return [_all_values[n] for n in names]

p200_TIPRACK_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Vertex","brandId":["4227-06"]},"metadata":{"displayName":"Vertex 96 Tip Rack 200 µL","displayCategory":"tipRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.75,"yDimension":85.47,"zDimension":60.16},"wells":{"A1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":75.27,"z":9.35},"B1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":65.87,"z":9.35},"C1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":56.47,"z":9.35},"D1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":47.07,"z":9.35},"E1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":37.67,"z":9.35},"F1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":28.27,"z":9.35},"G1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":18.87,"z":9.35},"H1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":9.47,"z":9.35},"A2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":75.27,"z":9.35},"B2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":65.87,"z":9.35},"C2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":56.47,"z":9.35},"D2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":47.07,"z":9.35},"E2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":37.67,"z":9.35},"F2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":28.27,"z":9.35},"G2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":18.87,"z":9.35},"H2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":9.47,"z":9.35},"A3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":75.27,"z":9.35},"B3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":65.87,"z":9.35},"C3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":56.47,"z":9.35},"D3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":47.07,"z":9.35},"E3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":37.67,"z":9.35},"F3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":28.27,"z":9.35},"G3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":18.87,"z":9.35},"H3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":9.47,"z":9.35},"A4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":75.27,"z":9.35},"B4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":65.87,"z":9.35},"C4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":56.47,"z":9.35},"D4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":47.07,"z":9.35},"E4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":37.67,"z":9.35},"F4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":28.27,"z":9.35},"G4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":18.87,"z":9.35},"H4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":9.47,"z":9.35},"A5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":75.27,"z":9.35},"B5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":65.87,"z":9.35},"C5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":56.47,"z":9.35},"D5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":47.07,"z":9.35},"E5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":37.67,"z":9.35},"F5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":28.27,"z":9.35},"G5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":18.87,"z":9.35},"H5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":9.47,"z":9.35},"A6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":75.27,"z":9.35},"B6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":65.87,"z":9.35},"C6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":56.47,"z":9.35},"D6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":47.07,"z":9.35},"E6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":37.67,"z":9.35},"F6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":28.27,"z":9.35},"G6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":18.87,"z":9.35},"H6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":9.47,"z":9.35},"A7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":75.27,"z":9.35},"B7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":65.87,"z":9.35},"C7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":56.47,"z":9.35},"D7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":47.07,"z":9.35},"E7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":37.67,"z":9.35},"F7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":28.27,"z":9.35},"G7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":18.87,"z":9.35},"H7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":9.47,"z":9.35},"A8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":75.27,"z":9.35},"B8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":65.87,"z":9.35},"C8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":56.47,"z":9.35},"D8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":47.07,"z":9.35},"E8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":37.67,"z":9.35},"F8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":28.27,"z":9.35},"G8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":18.87,"z":9.35},"H8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":9.47,"z":9.35},"A9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":75.27,"z":9.35},"B9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":65.87,"z":9.35},"C9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":56.47,"z":9.35},"D9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":47.07,"z":9.35},"E9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":37.67,"z":9.35},"F9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":28.27,"z":9.35},"G9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":18.87,"z":9.35},"H9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":9.47,"z":9.35},"A10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":75.27,"z":9.35},"B10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":65.87,"z":9.35},"C10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":56.47,"z":9.35},"D10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":47.07,"z":9.35},"E10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":37.67,"z":9.35},"F10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":28.27,"z":9.35},"G10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":18.87,"z":9.35},"H10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":9.47,"z":9.35},"A11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":75.27,"z":9.35},"B11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":65.87,"z":9.35},"C11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":56.47,"z":9.35},"D11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":47.07,"z":9.35},"E11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":37.67,"z":9.35},"F11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":28.27,"z":9.35},"G11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":18.87,"z":9.35},"H11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":9.47,"z":9.35},"A12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":75.27,"z":9.35},"B12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":65.87,"z":9.35},"C12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":56.47,"z":9.35},"D12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":47.07,"z":9.35},"E12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":37.67,"z":9.35},"F12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":28.27,"z":9.35},"G12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":18.87,"z":9.35},"H12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":9.47,"z":9.35}},"groups":[{"metadata":{},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":true,"tipLength":50.81,"isMagneticModuleCompatible":false,"loadName":"vertex_96_tiprack_200ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
Custom_Tiprack_DEF = json.loads(p200_TIPRACK_DEF_JSON)

metadata = {
    'protocolName': 'TNA extraction',
    'author': 'Multiplex <bvalderrama@multiplex.bio>',
    'description': 'Total nucleic acid extraction with 96 samples and a timer printed on screen for each incubation time',
    'source': 'Modified from Protocol Library',
    'apiLevel': '2.10'
    }


def run(protocol_context):

    [mag_mod, pipette_type, pipette_mount, sample_number, sample_volume,
     bead_ratio, elution_buffer_volume, incubation_time, settling_time,
     drying_time, custom_tiprack] = get_values(
        "mag_mod", "pipette_type", "pipette_mount", "sample_number",
        "sample_volume", "bead_ratio", "elution_buffer_volume",
        "incubation_time", "settling_time", "drying_time",
        "custom_tiprack"
    )

    ## Modules
    mag_deck = protocol_context.load_module(mag_mod, '1')
    mag_plate = mag_deck.load_labware('biorad_96_wellplate_200ul_pcr')
    
    
    ## Labware
    output_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '2', 'output plate')
    
    # Number (and position) of tipracks
    total_tips = sample_number*8
    tiprack_num = math.ceil(total_tips/96)
    slots = ['3', '5', '6', '7', '8', '9', '10', '11'][:tiprack_num]

    
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
    
    # Defining tipracks based whether they are custom or not
    if custom_tiprack == "yes":
        tipracks = [protocol_context.load_labware_from_definition(Custom_Tiprack_DEF, slot) for slot in slots]
    else:    
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
        # Many liquid waste wells due to the great amount of liquid used on each wash
        liquid_waste1 = reagent_container.wells()[-1] 
        liquid_waste2 = reagent_container.wells()[-2]
        liquid_waste3 = reagent_container.wells()[-3]
        liquid_waste4 = reagent_container.wells()[-4]
        
        col_num = math.ceil(sample_number/8)
        samples = [col for col in mag_plate.rows()[0][:col_num]]
        output = [col for col in output_plate.rows()[0][:col_num]]

        
    ## Labware 
    # Define the internal structure of the reagents containers
    beads = reagent_container.wells()[0]
    ethanol = reagent_container.wells()[1]
    ethanol2= reagent_container.wells()[2]
    ethanol_salt = reagent_container.wells()[3]
    elution_buffer = reagent_container.wells()[4]
    

    # Defining bead and mix volume
    bead_volume = sample_volume * bead_ratio #  bead_volume = 50 * 1

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
    pipette.well_bottom_clearance.aspirate = 1
    pipette.well_bottom_clearance.dispense = 5
    air_vol = pipette.max_volume * 0.1
    
    
    
	## The protocol begins:
    # Mix the beads and dispense them to sample
    for target in samples:
        pipette.pick_up_tip()
        pipette.mix(10, 50, beads)
        pipette.transfer(bead_volume, beads, target, new_tip='never')
        pipette.mix(20, 50, target)
        #pipette.blow_out(liquid_waste1) #|| Se eliminó este paso para evitar contaminación cruzada
        pipette.drop_tip()

    # Incubate sample with beads at RT for 15 minutes
    for i in range(incubation_time):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, incubation_time))

    # Engagae MagDeck and incubate
    mag_deck.engage(height=10)
        
    # Incubation time with iman for 7 mins
    for i in range(settling_time):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, settling_time))
        
    # Remove supernatant (total_vol = 50 uL from sample + 50 uL from beads + 5 extra uL) from magnetic beads 
    pipette.flow_rate.aspirate = 10
    pipette.flow_rate.dispense = 150
    
    for target in samples: 
        pipette.transfer(total_vol, target, liquid_waste1.top(), air_gap=air_vol, blow_out=True)

        
    # First wash: 130 uL of Ethanol salt (70% ethanol and NaCl 0.5M)
    # NOTE: All washing steps and the drying steps are done with the iman
    pipette.flow_rate.aspirate = 25
    
    #\ Try using same tip for all
    ####\ Maybe at this point do mixing per tip usage......
    mag_deck.disengage()
    for target in samples:
        pipette.pick_up_tip()
        pipette.transfer(130, ethanol_salt, target.top(), air_gap=air_vol, new_tip='never')
        pipette.mix(10, 75, target)
        pipette.blow_out(target.top(z=-0.5))
        pipette.touch_tip(target, v_offset=-0.5)
        pipette.drop_tip()

    mag_deck.engage(height=10)
    
    # Incubation with Ethanol salt and the iman for 5 minutes
    for i in range(5):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, 5))

    # Remove first wash (70% ethanol NaCl 5 M) 
    ## || All removals are done with the same tip 
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(130, target, liquid_waste2.top(), air_gap=air_vol, new_tip='never', blow_out = True, touch_tip=True)
        pipette.blow_out(target.top(z=-0.5)) # ||Quizás eliminarlo para no hacer esto 2 veces
        pipette.touch_tip(target, v_offset=-0.5) # ||Quizás eliminarlo para no hacer esto 2 veces
    pipette.drop_tip()

    
    # Second wash: 130 uL of Ethanol (70% ethanol)
    ## || All washes and removals are done with the same tip 
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(130, ethanol, target.top(), air_gap=air_vol, new_tip='never')
        pipette.blow_out(target.top(z=-0.5))
        pipette.touch_tip(target, v_offset=-0.5)

    # Incubation with Ethanol 70% for 1 minute
    protocol_context.delay(minutes=1)

    # Remove second wash (70% ethanol)
    ##\changed tips
    for target in samples:
        pipette.transfer(130, target, liquid_waste3.top(), air_gap=air_vol, new_tip='never', blow_out = True, touch_tip=True)
        pipette.blow_out(target.top(z=-0.5)) # ||Quizás eliminarlo para no hacer esto 2 veces
        pipette.touch_tip(target, v_offset=-0.5) # ||Quizás eliminarlo para no hacer esto 2 veces
    pipette.drop_tip()
    
    
    # Third wash: 130 uL of Ethanol (70% Ethanol)
    ##\ Try using same tip for all
    pipette.pick_up_tip()
    for target in samples:
        pipette.transfer(130, ethanol2, target.top(), air_gap=air_vol, new_tip='never')
        pipette.blow_out(target.top(z=-0.5))
        pipette.touch_tip(target, v_offset=-0.5)
    
    # Incubation with Ethanol 70% for 1 minute
    protocol_context.delay(minutes=1)
    
    # Carefully remove 70% ethanol
    ###\ I see ethanol sticking and falling on tip and on plate / reduce air volume? # || I think this was solved
    pipette.flow_rate.aspirate = 15 # slower aspirate rate than previous steps
    pipette.well_bottom_clearance.aspirate = 1
    for target in samples:
        pipette.transfer(145, target, liquid_waste4.top(), air_gap=air_vol, new_tip='never', blow_out = True, touch_tip=True) # This step removes more liquid than what the well actually has
        pipette.blow_out(target.top(z=-0.5)) # ||Quizás eliminarlo para no hacer esto 2 veces
        pipette.touch_tip(target, v_offset=-0.5) # ||Quizás eliminarlo para no hacer esto 2 veces
        
        #pipette.blow_out() #|| Hay que volver a usarlo en caso de volver a usar dos tomas de aire.
        #pipette.transfer(30, target, liquid_waste4.top(), air_gap=air_vol, new_tip='never') #|| No me parece que sea buena idea hacer que el opentrons pipetee tanto aire
        #pipette.blow_out() #|| No me parece que sea buena idea hacer que el opentrons pipetee tanto aire
    pipette.drop_tip()

    
    # Dry at RT for 5 minutes 
    for i in range(drying_time):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, drying_time))

    # Disengage MagDeck
    mag_deck.disengage()

    
    # Elution with 55 uL of elution buffer (ultra pure H2O) and then apply a strong mix
    pipette.flow_rate.aspirate = 50
    pipette.flow_rate.dispense = 300
    for target in samples:
        pipette.pick_up_tip()
        pipette.transfer(elution_buffer_volume+5, elution_buffer, target, new_tip='never')
        pipette.mix(20, mix_vol, target)
        pipette.blow_out(target.top(z=-0.5))
        pipette.touch_tip(target, v_offset=-0.5)
        pipette.drop_tip()

        
    # Incubation at RT for 1 minute    
    for i in range(5):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, 5))


    # Incubation with iman for 7 minutes
    mag_deck.engage(height=10)
    
    for i in range(settling_time):
        protocol_context.delay(minutes=1, msg= '{} minutes passed out of a total of {} minutes'.format(i, settling_time))
    
    
    # Transfer 50 uL of PCR product to a new well
    pipette.flow_rate.aspirate = 10
    for target, dest in zip(samples, output):
        pipette.transfer(elution_buffer_volume, target, dest, blow_out=True)