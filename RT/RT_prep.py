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
    _all_values = json.loads("""{"sample_number":8, "custom_sample_plate":"no", "custom_output_plate":"yes"}""")
    return [_all_values[n] for n in names]

def run(protocol):
    
    [sample_number,
     custom_tipracks, custom_sample_plate, custom_output_plate] = get_values(
        "sample_number",
        "custom_tipracks", "custom_sample_plate", "custom_output_plate"
    )
    
    
    # TIPS
    slots = ['4','7','8']  
    
    if custom_tipracks == 'yes':
        # Another tiprack will be used.
        tipracks = [protocol.load_labware('vertex_96_tiprack_200ul', slot, 'tiprack') for slot in slots]
        
    else:
        tipracks = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'tiprack') for slot in slots]
    
    
    
    # LABWARE:
    
    # RNA plates (96 well plates)
    if custom_sample_plate == 'yes':
        sample_plate = protocol.load_labware('nest_96_wellplate_200ul_cap', 1, 'plate with RNA samples')
        
    else:
        sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1, 'plate with RNA samples')
    
    col_number = math.ceil(sample_number/8)
    rna_samples = [col for col in sample_plate.rows()[0][:col_number]]
    
    
    # Output plate (96 well plastic + adapter)
    if custom_output_plate == 'yes':
        o_plate = protocol.load_labware('nest_96_wellplate_300ul_skirtless', 2, 'output plate')
        
    else:
        o_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2, 'output plate')
    
    
    
    # Rack with reagents (eppendorf tubes)
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 5, 'eppendorf rack')
    
    master_mix = eppendorf_rack.wells()[0]
    primer_h2o = eppendorf_rack.wells()[-1]
    
    
    
    # INSTRUMENTS
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks = tipracks)
    s20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks = tipracks)
    
    
    
    
    # COMMANDS

    # RT - PASO 1: Primers + H20
    vol_primers_h2o = sample_number*3 # Se necesitan 3 uL por muestra a procesar, por lo que se deben cargar originalmente un poco más de estos reactivos
    
    s20.flow_rate.aspirate = 100
    s20.flow_rate.dispense = 100
    s20.flow_rate.blow_out = 3
    
    s20.pick_up_tip()
    s20.mix(5, 20, primer_h2o) # Mixing the eppendorf with primers+h2o 5 times with 20 uL
    
    s20.distribute(3,
                   primer_h2o, # From
                   [o_plate.wells()[:sample_number]], #To
                   new_tip = 'never',
                   blow_out = True,
                   blowout_location = 'source well',
                   carryover = True # Split volumes when vol > pipette.max_volume
                  )
    
    s20.drop_tip()
    
    
    
    
    # RT - PASO 2: RNA
    volumen_templado = 2 #uL
    
    m20.flow_rate.aspirate = 20
    m20.flow_rate.dispense = 20
    m20.flow_rate.blow_out = volumen_templado
    
    output_samples = [col for col in o_plate.rows()[0][:col_number]]
    
    for rna_sample , output_sample in zip(rna_samples, output_samples):
        m20.pick_up_tip()
        m20.mix(3, 20, rna_sample)
        m20.aspirate(volumen_templado, rna_sample)
        m20.dispense(m20.current_volume, output_sample)
        
        m20.blow_out(output_sample.bottom(z=5))
        #m20.touch_tip(output_sample, v_offset = -0.5, speed = 50)
        
        m20.drop_tip()
        
        ## EL CÓDIGO DE ARRIBA SE PUEDE RESUMIR EN LO DE ABAJO. SIN EMBARGO, EL DE ARRIBA SE PUEDE PERSONALIZAR PARA REALIZAR LAS FUNCIONES DE LA PIPETA A DISTINTAS ALTURAS
        #m20.transfer(volumen_templado,
        #            rna_sample,
        #            output_sample,
        #            new_tip = 'always',
        #            blow_out = True,
        #            touch_tip = True)
    
    
    
    
    # RT - PASO 3: Incubación (Pausing the protocol)
    protocol.pause("Incubar el output plate por 5 minutos minutos a 65°C. Luego de la incubación, devuelvelo al sitio 2 y presiona 'Continuar' para seguir con el protocolo")
    
    
    
    
    # RT - PASO 4: Master Mix
    volumen_mastermix = 5 #uL
    
    output_samples = o_plate.wells()[:sample_number]
    
    s20.pick_up_tip()
    s20.mix(5, 20, master_mix)
    s20.drop_tip()
    
    s20.flow_rate.aspirate = 5
    s20.flow_rate.dispense = 5
    s20.flow_rate.blow_out = 5
    
    for output_sample in output_samples:
        s20.transfer(volumen_mastermix,
                     master_mix,
                     output_sample,
                     new_tip = 'always',
                     blow_out = True,
                     blowout_location = 'destination well')