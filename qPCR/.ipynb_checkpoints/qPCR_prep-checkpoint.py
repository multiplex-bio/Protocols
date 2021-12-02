# Inventario de cosas por implementar/mejorar:

# 1.- Aún no se prueba con replicates > 2.

import json
import math


metadata = {
    'protocolName': 'rt-PCR preparation protocol',
    'author': 'Multiplex <bvalderrama@multiplex.bio>',
    'description': 'Preparation of qPCR after RT',
    'source': 'Made by multiplex',
    'apiLevel': '2.11'
    }


def get_values(*names):
    # Los valores para que las variables custom_* funcione son "yes" o "no"
    
    # Máximo valor de RT_sample_number es 94
    _all_values = json.loads("""{"RT_sample_number":57,
    
    "custom_tiprack":"no", "custom_rt_plate":"no","custom_pcr_plate":"no", "replicates":2}""")
    return [_all_values[n] for n in names]


def run(protocol):
    
    [RT_sample_number,
     custom_tiprack, custom_rt_plate, custom_pcr_plate,
     replicates] = get_values(
        "RT_sample_number",
        "custom_tiprack", "custom_rt_plate", "custom_pcr_plate",
        "replicates"
    )
    
    # TIPS
    slots = ['5','8','11']
    special_slots = ['10']
    
    tipracks = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'tiprack') for slot in slots]
    special_tiprack = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'special tiprack') for slot in special_slots] # Tiprack for pipetting with less than 8 channels
    
    
    
    # INSTRUMENTS
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks = tipracks)
    s20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks = tipracks)
    
    
    
    # LABWARE:
    
    # Master Mix (Eppendorf tubes rack)
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 2, 'eppendorf rack')
    
    mastermix = eppendorf_rack.wells()[0] # A1
    eppendorf_con_control_positivo = eppendorf_rack.wells()[1] # B1
    eppendorf_con_control_negativo = eppendorf_rack.wells()[2] # C1
    
    
    
    
    # RT related labware:
    
    # Loading plates with the RT samples
    if custom_rt_plate == 'yes':
        rt_plate = protocol.load_labware('nest_96_wellplate_300ul_skirtless', 1, 'RT sample plate')
            
    else:
        rt_plate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1, 'RT sample plate')
    
    
    
    # rt-PCR related labware:
    
    # Calculating how many wells (samples + controls) we gonna use for RT:
    number_of_wells_for_rt = RT_sample_number + 4 # 2 controls for each step (Extraction and RT)
    
    # Therefore, we can know how many plates for rt-PCR we will use
    number_of_wells_for_pcr = number_of_wells_for_rt * replicates
    needed_pcr_plates = math.ceil(number_of_wells_for_pcr/96)

    
    # Loading the required plates for the rt-PCR ractions (rx) 
    pcr_slots = ['4','7'][:needed_pcr_plates]
    pcr_plates = [protocol.load_labware('biorad_96_wellplate_200ul_pcr', slot, 'q-PCR output plate') for slot in pcr_slots] # It need to be biorad plates as output PCR plate

    
    
    
    # ALL RIGHT UNTIL HERE
    # Custom function: Take a list of plates (or just one plate) and define which are columns are completed and which ones are incompleted
    def column_classifier(list_of_plates):
        
        col_number = math.ceil(RT_sample_number / 8)
        #print("\ncol_number : ", col_number)
        num_of_complete_cols_plate = divmod(RT_sample_number, 8)[0]
        #print("\nnum_of_complete_cols_rt_plate : ", num_of_complete_cols_rt_plate)
    
        
        if RT_sample_number % 8 == 0: # If all columns are full of samples
            
            # Check whether the input of the function was a list of plates ...
            if type(list_of_plates) == list:
                
                plate_complete_cols = [col for plate in list_of_plates for col in plate.rows()[0][:num_of_complete_cols_plate]]
                plate_incomplete_cols = [col for plate in list_of_plates for col in plate.rows()[0][num_of_complete_cols_plate:num_of_complete_cols_plate]]
                
            else: # or not (input was just one plate)
                
                plate_complete_cols = [col for col in list_of_plates.rows()[0][:num_of_complete_cols_plate]]
                #print("\nrt_complete_cols : ", rt_complete_cols)
                plate_incomplete_cols = [col for col in list_of_plates.rows()[0][num_of_complete_cols_plate:num_of_complete_cols_plate]] # Empty list
                #print("\nrt_incomplete_cols : ", rt_incomplete_cols)
        
        
        
        else: # There are no incomplete cols
            
            # Check whether the input of the function was a list of plates ...
            if type(list_of_plates) == list:
                
                plate_complete_cols = [col for plate in list_of_plates for col in plate.rows()[0][:num_of_complete_cols_plate]]
                plate_incomplete_cols = [col for plate in list_of_plates for col in plate.rows()[0][num_of_complete_cols_plate:col_number]]
                
            else: # or not (input was just one plate)
                plate_complete_cols = [col for col in list_of_plates.rows()[0][:num_of_complete_cols_plate]]
                #print("\nrt_complete_cols : ", rt_complete_cols)
                plate_incomplete_cols = [col for col in list_of_plates.rows()[0][num_of_complete_cols_plate:col_number]] # Empty list
                #print("\nrt_incomplete_cols : ", rt_incomplete_cols)
        
        
        return [plate_complete_cols, plate_incomplete_cols] # Subset the function's output with 0 for complete columns and 1 for incomplete columns.
    
    
    
    
    # Custom function: It makes a flat list out of a nested list
    def list_flattener(list):
        return [item for sublist in list for item in sublist]
    
    
    
    
    # Custom function : Takes a list of plates (or just one plate), slice each of them on the half and gives just *one flat* list for each side of all plates on the list
    def slice_list_of_plates(list_of_plates, plate_type): # plate_type puede ser rt o qpcr
     
        # Check whether list of plates was indeed a list of paltes
        if plate_type == "qpcr": 
            nested_plates = [plate.rows()[0] for plate in list_of_plates]
            
            nested_plates_left = [plate[:len(plate)//2] for plate in nested_plates]
            nested_plates_right = [plate[len(plate)//2:] for plate in nested_plates]
            
            if len(pcr_slots) > 1:
            
                first_replicate_plate = [nested_plates_left[0], nested_plates_right[0]]
                second_replicate_plate = [nested_plates_left[1], nested_plates_right[1]]
                plates_with_replicates = [first_replicate_plate, second_replicate_plate]
            
            else:    
                plates_with_replicates = [nested_plates_left[0], nested_plates_right[0]]
            
            return plates_with_replicates
        
        elif plate_type == "rt": # Or, on the other hand, if it was just one plate
        
            plate_left = list_of_plates.rows()[0][:len(list_of_plates.columns())//replicates]
            plate_right = list_of_plates.rows()[0][len(list_of_plates.columns())//replicates:]
        
            return [plate_left, plate_right] # Subset the function's output with 0 for left and 1 for right side.
    
    
    
    
    # PLATES SLICED:
    rt_plate_left = slice_list_of_plates(rt_plate, "rt")[0]
    rt_plate_right = slice_list_of_plates(rt_plate, "rt")[1]

    
    
    nested_list_plates_and_halves = slice_list_of_plates(pcr_plates, "qpcr")

    pcr_plate_rep1 = nested_list_plates_and_halves[0]
    pcr_plate_rep2 = nested_list_plates_and_halves[1]

    
    
    
    
    
    
    # LIST WITH ALL THE COMPLETE AND INCOMPLETE COLUMNS IN RT_PLATE
    rt_plate_complete_cols = column_classifier(rt_plate)[0]
    rt_plate_incomplete_cols = column_classifier(rt_plate)[1]

    
    
    
    
    # COMPLETE AND INCOMPLETE COLUMNS IN THE RT_PLATE BY SIDE 
    rt_comp_cols_left = [col for col in rt_plate_left if col in rt_plate_complete_cols]
    rt_incomp_cols_left = [col for col in rt_plate_left if col in rt_plate_incomplete_cols]
    
    rt_comp_cols_right = [col for col in rt_plate_right if col in rt_plate_complete_cols]
    rt_incomp_cols_right = [col for col in rt_plate_right if col in rt_plate_incomplete_cols]
    
    
    
    
    # LIST WITH ALL THE COMPLETE AND INCOMPLETE COLUMNS IN PCR_PLATE
    
    pcr_plates_complete_cols = column_classifier(pcr_plates)[0]
    pcr_plates_incomplete_cols = column_classifier(pcr_plates)[1]
    
    
    
    # COMPLETE AND INCOMPLETE COLUMNS IN THE PCR_PLATE BY SIDE 
    
    if len(pcr_slots) <= 1:
        pcr_comp_cols_rep1 = [col for col in pcr_plate_rep1 if col in pcr_plates_complete_cols]
        pcr_incomp_cols_rep1 = [col for col in pcr_plate_rep1 if col in pcr_plates_incomplete_cols]
    
        pcr_comp_cols_rep2 = [col for col in pcr_plate_rep2[:len(pcr_comp_cols_rep1)]]
        pcr_incomp_cols_rep2 = [pcr_plate_rep2[len(pcr_comp_cols_rep1)]]
        
    
    else:
        pcr_comp_cols_rep1 = [col for side in pcr_plate_rep1 for col in side if col in pcr_plates_complete_cols]
        pcr_incomp_cols_rep1 = [col for side in pcr_plate_rep1 for col in side if col in pcr_plates_incomplete_cols]
        
        pcr_comp_cols_rep2 = [col for side in pcr_plate_rep2 for col in side if col in pcr_plates_complete_cols]
        pcr_incomp_cols_rep2 = [col for side in pcr_plate_rep2 for col in side if col in pcr_plates_incomplete_cols]
        pass
    
    
    
    pairs_of_rep_cols_comp = [[pcr_comp_cols_rep1[i], pcr_comp_cols_rep2[i]] for i in range(len(pcr_comp_cols_rep1))]
    pairs_of_rep_cols_incomp = [[pcr_incomp_cols_rep1[i], pcr_incomp_cols_rep2[i]] for i in range(len(pcr_incomp_cols_rep1))]
    
    
    
    
    
    # COMMANDS
    
    # qPCR - PASO 1: 14.25 uL de Master Mix desde el eppendorf tube rack hacia en cada pocillo del PCR plate
    protocol.comment("\nMaster Mix")
    mastermix_volume = 14.25
    output_wells= [well for plate in pcr_plates for well in plate.wells()[:RT_sample_number+2]] # +2 due to the two new controls
    
    s20.flow_rate.aspirate = 2
    s20.flow_rate.dispense = 2
    s20.flow_rate.blow_out = 1
    
    
    for well in output_wells:
        s20.pick_up_tip()
        s20.aspirate(mastermix_volume, mastermix)
        s20.dispense(s20.current_volume, well.bottom())
        s20.blow_out(well.top(z=-1))
        s20.touch_tip(v_offset=-0.5, speed = 50)
        s20.drop_tip()
        
    
    
    
    
    # qPCR - PASO 2: 0.75 uL de Templado desde el RT plate hacia el PCR plate
    template_volume = 1
    pairs_of_rep_cols_comp = [[pcr_comp_cols_rep1[i], pcr_comp_cols_rep2[i]] for i in range(len(pcr_comp_cols_rep1))]
    
    
    # TRANSFER TO COMPLETE COLUMNS
    protocol.comment("\nComplete Columns")
    
    m20.flow_rate.aspirate = 5
    m20.flow_rate.dispense = 5
    m20.flow_rate.blow_out = 1
    
    
    for col in range(len(pairs_of_rep_cols_comp)):
        m20.transfer(template_volume,
                     rt_plate_complete_cols[col],
                     pairs_of_rep_cols_comp[col],
                     new_tip = 'always',
                     blow_out = True,
                     blowout_location = 'destination well',
                     touch_tip = True)
    
    
    
    
    
    # TRANSFER TO INCOMPLETE COLUMNS
    protocol.comment("\nIncomplete Columns")

    # Replace the m20 pipette with the same pipette. This will allow us to use it with the special tiprack
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', replace = True)  
    
    m20.flow_rate.aspirate = 5
    m20.flow_rate.dispense = 5
    m20.flow_rate.blow_out = 1
    
    if RT_sample_number % 8 == 0: 
        # If the colum will be filled when we add the controls, then we have 6 samples in the incomplete colum
        num_wells_on_incomplete_cols = 6
        
    else:
        num_wells_on_incomplete_cols = divmod(RT_sample_number, 8)[1]
    
    
    num_channels_per_pickup = num_wells_on_incomplete_cols

    
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
    
    
    print("pairs_of_rep_cols_incomp : ", pairs_of_rep_cols_incomp)
    
    for col in range(len(pairs_of_rep_cols_incomp)):
        special_pick_up(m20)
        m20.transfer(template_volume,
                     rt_plate_incomplete_cols[col],
                     pairs_of_rep_cols_incomp[col],
                     new_tip = 'never')
    
    
    
    
    # qPCR - PASO 3: 0.75 uL de Control +/- desde el eppendorf tuberack hacia el PCR plate
    
    if len(pcr_slots) < 2:
        
        output_wells_control_positivo_right = [plate.wells()[RT_sample_number+len(rt_plate.wells())//replicates] for plate in pcr_plates]
    
        output_wells_control_positivo_left = [plate.wells()[RT_sample_number] for plate in pcr_plates]
    
        output_wells_control_negativo_right = [plate.wells()[RT_sample_number+1+len(rt_plate.wells())//replicates] for plate in pcr_plates]
        
        output_wells_control_negativo_left = [plate.wells()[RT_sample_number+1] for plate in pcr_plates]
        

        
        output_wells_controles_positivos = list_flattener([output_wells_control_positivo_left, output_wells_control_positivo_right])
        output_wells_controles_negativos = list_flattener([output_wells_control_negativo_left, output_wells_control_negativo_right])
        
        
        
    else:
        
        output_wells_controles_positivos = [plate.wells()[RT_sample_number] for plate in pcr_plates]
        output_wells_controles_negativos = [plate.wells()[RT_sample_number+1] for plate in pcr_plates]
        
        
        
    
    
    
    # Control +
    protocol.comment("\nControl +")
    
    s20.pick_up_tip()
    for well in output_wells_controles_positivos:
        s20.aspirate(template_volume, eppendorf_con_control_positivo)
        s20.dispense(s20.current_volume, well)
        s20.blow_out(well.top(z=-0.5))
        s20.touch_tip(v_offset = -0.5, speed = 50)
    s20.drop_tip()
        

    
    
    # Control -
    protocol.comment("\nControl -")
    
    s20.pick_up_tip()
    for well in output_wells_controles_negativos:
        s20.aspirate(template_volume, eppendorf_con_control_negativo)
        s20.dispense(s20.current_volume, well)
        s20.blow_out(well.top(z=-0.5))
        s20.touch_tip(v_offset = -0.5, speed = 50)
    s20.drop_tip()
        

        
        
    
    # qPCR - PASO 4: Realizar el qPCR
    if len(pcr_slots) <= 1:
        protocol.pause("Retirar las output plates (slot '4') y realizar el programa de qPCR en el termociclador")
    else:
        protocol.pause("Retirar las output plates (slots '4' y '7') y realizar el programa de qPCR en el termociclador")
    