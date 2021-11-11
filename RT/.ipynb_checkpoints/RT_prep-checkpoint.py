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
    # Aun no se puede usar custom tiprack
    _all_values = json.loads("""{"sample_number":20,"custom_tiprack":"no", "custom_output_plate":"no"}""")
    return [_all_values[n] for n in names]

def run(protocol):
    
    [sample_number,
     custom_tiprack, custom_output_plate] = get_values(
        "sample_number",
        "custom_tiprack", "custom_output_plate"
    )
    
    
    # TIPS
    if custom_tiprack == 'yes':
        big_tiprack = [protocol.load_labware('vertex_96_tiprack_200ul', 6, 'big tips tiprack')]
    else:
        big_tiprack = [protocol.load_labware('opentrons_96_tiprack_300ul', 6, 'big tips tiprack')]
    
    
    small_tiprack = [protocol.load_labware('opentrons_96_tiprack_20ul', 4, 'smal tips tiprack')]
    
    
    
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
    
    
    # Mastermix
    #mastermix_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3, 'master mix rack')
    
    # Primer plates (custom eppendorfs rack)
    #primerh20_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 5, 'Primers+H2O rack')
    
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 3, 'eppendorf rack')
    
    master_mix = eppendorf_rack.wells()[0]
    primer_h20 = eppendorf_rack.wells()[-1]
    
    
    
    # INSTRUMENTS
    m20 = protocol.load_instrument('p20_multi_gen2', 'left', tip_racks = small_tiprack)
    s300 = protocol.load_instrument('p300_single_gen2', 'right', tip_racks = big_tiprack)
    
    
    
    # COMMANDS
    
    # RT - PASO 1: Primers + H20
    vol_primers_h2o = sample_number*3 # Se necesitan 3 uL por muestra a procesar, por lo que se deben cargar originalmente un poco más de estos reactivos
    disposal_volume = vol_primers_h2o*0.15
    
    s300.distribute(3,
                    master_mix, # From
                    [o_plate.wells()[:sample_number]], #To
                    mix_before = (5, vol_primers_h2o - 2), # Mixing vol_primers_h2o 5 times
                    blow_out = True,
                    carryover = False,
                    disposal_volume = disposal_volume
                   )
    
    
    
    # Incubación (Pausing the protocol)
    protocol.comment("Incubar por X minutos")
    protocol.pause("Coloca el output plate en el sitio 2 y presiona 'Continuar' para seguir con el resto del protocolo")
    
    
    
    # RT - PASO 2: RNA
    output_samples = [col for col in o_plate.rows()[0][:col_number]]
    
    volumen_templado = 2 #uL
    
    for rna_sample , output_sample in zip(rna_samples, output_samples):
        m20.pick_up_tip()
        m20.mix(5, 15, rna_sample)
        m20.aspirate(volumen_templado, rna_sample)
        m20.dispense(m20.current_volume, output_sample.top(z=-5))
        
        # Puede que se elimine el blow_out y touch_tip
        m20.blow_out(output_sample.top(z=-5))
        m20.touch_tip(output_sample, v_offset = -0.5, speed = 50)
        
        m20.drop_tip()
        
        #m20.transfer(volumen_templado,
        #            rna_sample,
        #            output_sample,
        #            new_tip = 'always',
        #            blow_out = True,
        #            touch_tip = True)
    
    
    
    # RT - PASO 3: Master Mix
    output_samples = o_plate.wells()[:sample_number]
    volumen_mastermix = 5 #uL
    
    for output_sample in output_samples:
        s300.transfer(volumen_mastermix,
                     master_mix,
                     output_sample)
        
    