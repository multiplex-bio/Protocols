import json
import math


metadata = {
    'protocolName': 'RT preparation',
    'author': 'Multiplex <bvalderrama@multiplex.bio>',
    'description': 'Preparation of the Retro-transcription of RNA samples',
    'source': 'Made by multiplex',
    'apiLevel': '2.11'
    }


def get_values(*names):
    # los valores para que las variables custom_* funcione son "yes" o "no"
    _all_values = json.loads("""{"sample_number":8,"custom_tiprack":"no", "custom_output_plate":"no"}""")
    return [_all_values[n] for n in names]

def run(protocol):
    
    [sample_number,
     custom_tiprack, custom_output_plate] = get_values(
        "sample_number",
        "custom_tiprack", "custom_output_plate"
    )
    
    
    # TIPS
    slots = ['4','6','9']
    
    
    # When this protocol was intended to work with p300 single channel instead of p20 single channel. We decline to go further with this idea due to the low accuracy
    #if custom_tiprack == 'yes':
    #    big_tiprack = [protocol.load_labware('vertex_96_tiprack_200ul', slot, 'big tips tiprack') for slot in slots]
    #else:
    #    big_tiprack = [protocol.load_labware('opentrons_96_tiprack_300ul', slot, 'big tips tiprack') for slot in slots]
    
    
    small_tiprack = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'small tips tiprack') for slot in slots]
    
    
    
    # LABWARE:
    
    # RNA plates (96 well plates)
    if custom_output_plate == 'yes':
        sample_plate = protocol.load_labware('spl_96_wellplate_200ul_with_cap', 1, 'plate with RNA samples')
        
    else:
        sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1, 'plate with RNA samples')
    
    col_number = math.ceil(sample_number/8)
    rna_samples = [col for col in sample_plate.rows()[0][:col_number]]
    
    
    # Output plate (96 well plastic + adapter)
    o_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2, 'output plate') # The adapter makes it the same size as the biorad wellplate
    
    
    # Rack with reagents (eppendorf tubes)
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3, 'eppendorf rack')
    
    master_mix = eppendorf_rack.wells()[0]
    primer_h2o = eppendorf_rack.wells()[-1]
    
    
    
    # INSTRUMENTS
    #s300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks = big_tipracks)
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks = small_tiprack)
    s20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks = small_tiprack)
    
    
    
    # COMMANDS

    # RT - PASO 1: Primers + H20
    vol_primers_h2o = sample_number*3 # Se necesitan 3 uL por muestra a procesar, por lo que se deben cargar originalmente un poco más de estos reactivos
    #disposal_volume = vol_primers_h2o*0.15
    
    s20.distribute(3,
                    primer_h2o, # From
                    [o_plate.wells()[:sample_number]], #To
                    mix_before = (5, 20), # Mixing vol_primers_h2o 5 times
                    blow_out = True,
                    blowout_location = 'source well',
                    carryover = True # Split volumes when vol > pipette.max_volume
                    #disposal_volume = disposal_volume
                   )