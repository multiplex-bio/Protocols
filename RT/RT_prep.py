# Inventario de cosas por implementar/mejorar:

# 3.- Agregar un condicional en el transfer final, de forma que la punta que se usó para el mixing del mastermix se pueda usar en la primera transferencia hacia el output plate. Luego, las 
#     siguientes transferencias deben hacerse con una tip nueva.


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
    # Sample number = cantidad de muestras + 4 controles (positivo y negativo de la extracción y RT)
    
    # los valores para que las variables custom_* funcione son "yes" o "no"
    _all_values = json.loads("""{"sample_number":18, 
    
    "custom_tipracks":"no" , "custom_sample_plate":"no", "custom_output_plate":"no"}""") 
    return [_all_values[n] for n in names]

def run(protocol):
    
    [sample_number,
     custom_tipracks, custom_sample_plate, custom_output_plate] = get_values(
        "sample_number",
        "custom_tipracks", "custom_sample_plate", "custom_output_plate"
    )
    
    
    # TIPS
    slots = ['7','8','11']  
    special_slot = ['4']
    
    if custom_tipracks == 'yes':
        # Aún no existe necesidad de crear unas puntas custom de 20 uL. Cuando sea necesario se crearán y se va a actualizar el código.
        tipracks = [protocol.load_labware('vertex_96_tiprack_200ul', slot, 'tiprack') for slot in slots]
        special_tiprack = [protocol.load_labware('vertex_96_tiprack_200ul', slot, 'Special tiprack') for slot in special_slot]
    
    else:
        tipracks = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'tiprack') for slot in slots]
        special_tiprack = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'Special tiprack') for slot in special_slot]
    
    
    
    # LABWARE:
    
    
    
    
    # RNA plates (96 well plates)
    if custom_sample_plate == 'yes':
        sample_plate = protocol.load_labware('nest_96_wellplate_200ul_cap', 1, 'plate with RNA samples')
        
    else:
        sample_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1, 'plate with RNA samples')
    
    
    col_number = math.ceil(sample_number/8)
    num_of_complete_cols = divmod(sample_number, 8)[0]

    
    # COMPLETE COLS IN RNA PLATE: Where are them    
    rna_samples_complete_cols = [col for col in sample_plate.rows()[0][:num_of_complete_cols]]
    #print("rna_samples_complete_cols: ", rna_samples_complete_cols)
    
    
    # INCOMPLETE COLS IN RNA PLATE: Where are them
    rna_samples_incomplete_cols = [col for col in sample_plate.rows()[0][num_of_complete_cols:col_number]]
    #print("rna_samples_incomplete_cols : ", rna_samples_incomplete_cols)
    
    
    
    
    
    
    # Output plate (96 well plastic + adapter)
    if custom_output_plate == 'yes':
        o_plate = protocol.load_labware('nest_96_wellplate_300ul_skirtless', 2, 'output plate')
        
    else:
        o_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2, 'output plate')
    
    
    # COMPLETE COLS IN OUTPUTPLATE: Where are them
    output_samples_complete_cols = [col for col in o_plate.rows()[0][:num_of_complete_cols]]
    #print("output_samples_complete_cols: ", output_samples_complete_cols)
    
    # INCOMPLETE COLS IN OUTPUT PLATE: Where are them
    output_samples_incomplete_cols= [col for col in o_plate.rows()[0][num_of_complete_cols:col_number]]
    #print("output_samples_incomplete_cols : ", output_samples_incomplete_cols)
    
    
    
    
    
    
    
    # Rack with reagents (eppendorf tubes)
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 5, 'eppendorf rack')
    
    primer_h2o = eppendorf_rack.wells()[0] # A1
    ctrl_positivo = eppendorf_rack.wells()[1] # B1
    ctrl_negativo = eppendorf_rack.wells()[2] # C1
    master_mix = eppendorf_rack.wells()[3] # D1
    
    
    # INSTRUMENTS
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks = tipracks)
    s20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks = tipracks)
    
    
    
    
    # COMMANDS

    # RT - PASO 1: Primers + H20
    protocol.comment("Primers y H2O")
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
    protocol.comment("RNA")
    volumen_templado = 2 #uL
    
    m20.flow_rate.aspirate = 20
    m20.flow_rate.dispense = 20
    m20.flow_rate.blow_out = volumen_templado
    
    #output_samples = [col for col in o_plate.rows()[0][:col_number]]
    
    
    # Complete cols
    protocol.comment("Complete cols")
    
    for rna_sample , output_sample in zip(rna_samples_complete_cols, output_samples_complete_cols):
        m20.pick_up_tip()
        m20.mix(3, 20, rna_sample)
        m20.aspirate(volumen_templado, rna_sample.bottom()) # El bottom le da la profundidad necesaria para sacar 2uL del plate porque el diseño del palte me quedó un poco más alto de lo que es
        m20.dispense(m20.current_volume, output_sample)
        
        m20.blow_out(output_sample.bottom(z=5))
        
        m20.drop_tip()
    
    
    
    # Replace the m20 pipette with itself. This will allow us to use it with the special tiprack
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', replace = True)  
    
    
    num_wells_on_incomplete_cols = divmod(sample_number, 8)[1]
    num_channels_per_pickup = num_wells_on_incomplete_cols
    # (only pickup tips on front-most channel)

    per_tip_pickup_current = 0.075
    # (current required for picking up one tip, do not modify unless
    # you are using a GEN2 P300 8-Channel in which case change it to 
    # 0.1)
    # (for GEN2 P20 8-Channel, current must be 0.075)

    pick_up_current = num_channels_per_pickup*per_tip_pickup_current
    
    protocol._implementation._hw_manager.hardware._attached_instruments[
    m20._implementation.get_mount()
    ].update_config_item('pick_up_current', pick_up_current)
    
    
    # List of tips. Ordered based on the num_channels_per_pickup selected before.
    tips_ordered = [
    tip for rack in special_tiprack
       for row in rack.rows()[    
       len(rack.rows())
       -num_channels_per_pickup::-1*num_channels_per_pickup]
       for tip in row]
    
    tip_count = 0
    
    def special_pick_up(pip):
      nonlocal tip_count
      pip.pick_up_tip(tips_ordered[tip_count])
      tip_count += 1
    
    
    
    protocol.comment("Incomplete cols")
    
    for rna_sample , output_sample in zip(rna_samples_incomplete_cols, output_samples_incomplete_cols):
        special_pick_up(m20)
        m20.mix(3,20, rna_sample) #FIX
        m20.aspirate(volumen_templado, rna_sample.bottom()) # El bottom le da la profundidad necesaria para sacar 2uL.
        m20.dispense(m20.current_volume, output_sample)
        m20.blow_out(output_sample.bottom(z=5))
        m20.drop_tip()
    
    
    
    
    
    
    # Additionally, we determine the position for the RT controls (positive and negative, IN THIS EXACT ORDER)
    output_well_with_positive_control = o_plate.wells()[sample_number-2] # The well before the last well. -2 Because python starts its lists at 0
    output_well_with_negative_control = o_plate.wells()[sample_number-1] # Last well
    
    # Ctrl + 
    s20.flow_rate.aspirate = 20
    s20.flow_rate.dispense = 20
    s20.flow_rate.blow_out = volumen_templado
    
    protocol.comment("Ctrl +")
    s20.pick_up_tip()
    s20.mix(3, 20, ctrl_positivo) # Eppendorf with the positive control
    s20.aspirate(volumen_templado, ctrl_positivo)
    s20.dispense(s20.current_volume, output_well_with_positive_control)
    s20.blow_out(output_well_with_positive_control.bottom(z=5))
    s20.touch_tip(output_well_with_positive_control, v_offset = -0.5, speed = 50)
    s20.drop_tip()
    
    # Ctrl - 
    protocol.comment("Ctrl -")

    s20.pick_up_tip()
    s20.mix(3, 20, ctrl_negativo) # Eppendorf with the negative control
    s20.aspirate(volumen_templado, ctrl_negativo)
    s20.dispense(s20.current_volume, output_well_with_negative_control)
    s20.blow_out(output_well_with_negative_control.bottom(z=5))
    s20.touch_tip(output_well_with_negative_control, v_offset = -0.5, speed = 50)
    s20.drop_tip()
    
    
    
    
    
    # RT - PASO 3: Incubación (Pausing the protocol)
    protocol.pause("Incubar el output plate (ubicado en '2') por 5 minutos minutos a 65°C. Luego, devuelvelo a su sitio y presiona 'Continuar' para seguir con el protocolo")
    
    
    
    
    
    # RT - PASO 4: Master Mix
    protocol.comment("Master Mix")
    volumen_mastermix = 5 #uL
    
    
    s20.pick_up_tip()
    s20.mix(5, 20, master_mix)
    s20.drop_tip()
    
    s20.flow_rate.aspirate = 5
    s20.flow_rate.dispense = 5
    s20.flow_rate.blow_out = 5
    
    output_samples = o_plate.wells()[:sample_number]
    
    for output_sample in output_samples:
        s20.transfer(volumen_mastermix,
                     master_mix,
                     output_sample,
                     new_tip = 'always',
                     blow_out = True,
                     blowout_location = 'destination well')