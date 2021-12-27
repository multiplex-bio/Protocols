# LISTA DE COSAS POR HACER:

# HACER QUE SE PUEDAN TOMAR LAS PUNTAS DEL TIPRACK CON MENOS DE 8 CANALES DE ACUERDO A CUANTAS PUNTAS VAYA A NECESITAR

import json


metadata = {
    'protocolName': 'RT sample distribution',
    'author': 'Multiplex <bvalderrama@multiplex.bio>',
    'description': 'RTs samples distribution',
    'source': 'Made by multiplex',
    'apiLevel': '2.11'
    }


def get_values(*names):
    # Sample number = cantidad de muestras incluidos los controles positivo y negativo de la extracción
    
    # los valores para que las variables custom_* funcione son "yes" o "no"
    
    # La variable 'sample_number' puede tomar hasta 3 valores. 
    
    # Ejemplo 1: [19, 53, 40]. Esto quiere decir que el primer plate tiene 19 muestras, el segundo 53, y el tercero 40
    # Ejemplo 2: [50]. Esto quiere decir que se va a procesar sólo una placa y que esta tiene 50 muestras
    _all_values = json.loads("""{"sample_number":[16, 5, 24],
    
    "custom_tipracks":"no" , "custom_sample_plate":"no", "custom_output_plate":"no"}""") 
    return [_all_values[n] for n in names]

def run(protocol):
    
    [sample_number,
     custom_tipracks, custom_sample_plate, custom_output_plate] = get_values(
        "sample_number",
        "custom_tipracks", "custom_sample_plate", "custom_output_plate"
    )
    
    
    
    # LABWARE DEFINITION:
    
    print("\nsample_number : ", sample_number)
    #print("\nlen sample_number : ", len(sample_number))
    
    # RNA plates (96 well plates)
    samples_slots = ['4', '5', '6'][:len(sample_number)]
    
    if custom_sample_plate == 'yes':
        sample_plates = [protocol.load_labware('nest_96_wellplate_200ul_cap', slot, 'plate with RNA samples') for slot in samples_slots]
    else:
        sample_plates = [protocol.load_labware('biorad_96_wellplate_200ul_pcr', slot, 'plate with RNA samples') for slot in samples_slots]
    
    
    
    
    # Output plates
    output_slots = ['1', '2', '3'][:len(sample_number)]
    
    if custom_output_plate == 'yes':
        output_plates = [protocol.load_labware('nest_96_wellplate_300ul_skirtless', slot, 'output plate') for slot in output_slots]
    else:
        output_plates = [protocol.load_labware('biorad_96_wellplate_200ul_pcr', slot, 'output plate') for slot in output_slots]
        
        
        
    # Tips
    tip_slots = ['7', '8', '9'][:len(sample_number)]
    #print("\ntip_slots : ", tip_slots)
    if custom_tipracks == 'yes':
        # Las custom tipracks para p20 no están implementadas aún.
        tipracks = [protocol.load_labware('vertex_96_tiprack_20ul', slot, 'tiprack') for slot in tip_slots]
    else:
        tipracks = [protocol.load_labware('opentrons_96_tiprack_20ul', slot, 'tiprack') for slot in tip_slots]
     
    
    
    
    # Eppendorf tube rack
    eppendorf_rack = protocol.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', 11, 'eppendorf rack')
    
    eppendorf_control_positivo = eppendorf_rack.wells()[0] # A1
    eppendorf_control_negativo = eppendorf_rack.wells()[-1] # D6
    
    
    
    
    
    # INSTRUMENTS:
    m20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks = tipracks)
    s20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks = tipracks)
    
    
    
    
    
    #Quiero que se traspasen las muestras desde una columna del sample_plate a una columna del output_plate. Para eso es importante que antes haga el checkeo de cuantas puntas debe tomar para realizar el traspaso.
    
    # PREPARACIÓN:
    
    
    
    # NUMERO DE COLUMNAS COMPLETAS Y NUMERO DE POCILLOS CON MUESTRAS EN LA COLUMNA QUE QUEDA INCOMPLETA
    
    # Por 'num_cols_completas' sabemos el número de columnas completas que hay en cada placa.
    num_cols_completas = [divmod(number, 8)[0] for number in sample_number]
    #print("\nnum_cols_completas : ", num_cols_completas)
    
    # Por 'num_pocillos_col_incompleta' sabemos cuantos pocillos de la columna incompleta tienen muestras, lo que nos permite tomar el número exacto de puntas necesarias.
    num_pocillos_col_incompleta = [divmod(number, 8)[1] for number in sample_number]
    #print("\nnum_pocillos_col_incompleta : ", num_pocillos_col_incompleta)
    
    

    
    
    # LISTA CON LAS COLUMNAS COMPLETAS EN CADA RACK
    protocol.comment("\nCOMPLETE COLUMNS :")
    
    # La 'list_of_complete_columns_through_racks' es una lista. Cada elemento es, a su vez, una lista con todas las columnas que están completas de muestras
    list_of_complete_columns_through_sample_plates = []
    
    for num, plate in zip(num_cols_completas, sample_plates):
            for col in plate.rows()[0][:num]:
                list_of_complete_columns_through_sample_plates.append(col)

    #print("\nlist_of_complete_columns_through_sample_plates : ", list_of_complete_columns_through_sample_plates)            
    
    
    
    
    
    list_of_complete_columns_through_output_plates = []
    
    for num, plate in zip(num_cols_completas, output_plates):
            for col in plate.rows()[0][:num]:
                list_of_complete_columns_through_output_plates.append(col)

    #print("\nlist_of_complete_columns_through_output_plates : ", list_of_complete_columns_through_output_plates)
        
        
        

    
    # Transfering the RNA from sample_plates to output_plates (Complete columns only)
    
    lista_de_tips = []
    for rack, numero in zip(tipracks, num_cols_completas):
        lista_de_tips.append(rack.rows()[0][:numero])
    
    lista_de_tips = [subelement for element in lista_de_tips for subelement in element] # Make the previous list 'lista_de_puntas' a flat list
    
    for sample_col, output_col, tip_col in zip(list_of_complete_columns_through_sample_plates, list_of_complete_columns_through_output_plates, lista_de_tips):
        m20.pick_up_tip(tip_col)
        #m20.mix(20, 5, sample_col)
        m20.aspirate(2, sample_col)
        m20.dispense(2, output_col)
        m20.touch_tip(v_offset=-0.5, speed=50)
        m20.drop_tip()
        
    
    
    
    
    
    # Transfering the RNA from sample_plates to output_plates (Incomplete columns only)
    protocol.comment("\nINCOMPLETE COLUMNS :")
    
    
    # LISTA CON LAS COLUMNAS INCOMPLETAS EN CADA RACK
        
    # La 'list_of_incomplete_columns_through_racks' es una lista. Cada elemento es, a su vez, una lista con todas las columnas que no están completas
    list_of_incomplete_columns_through_sample_plates = []
    
    for num_complete, num_incomplete, plate in zip(num_cols_completas, num_pocillos_col_incompleta, sample_plates):
        if num_incomplete == 0: # Si el número de pocillos en la columna incompleta es == 0 (es deci, esa plate no tiene columnas incompletas), se pasa al siguiente plate
            list_of_incomplete_columns_through_sample_plates.append(None)
        else: 
            # En caso de que el plate tenga una columna incompleta, se guarda cuantos pocillos tienen esa columna incompleta para que la pipeta tome el número exacto de tips necesarios
            for col in plate.rows()[0][num_complete:num_complete+1]:
                list_of_incomplete_columns_through_sample_plates.append(col)
    
    #print("\nlist_of_incomplete_columns_through_sample_plates : ", list_of_incomplete_columns_through_sample_plates)
    
    
    
    
    list_of_incomplete_columns_through_output_plates = []
    
    for num_complete, num_incomplete, plate in zip(num_cols_completas, num_pocillos_col_incompleta, output_plates):
        if num_incomplete == 0: # Si el número de pocillos en la columna incompleta es == 0 (es deci, esa plate no tiene columnas incompletas), se pasa al siguiente plate
            list_of_incomplete_columns_through_output_plates.append(None)
        else: 
            # En caso de que el plate tenga una columna incompleta, se guarda cuantos pocillos tienen esa columna incompleta para que la pipeta tome el número exacto de tips necesarios
            for col in plate.rows()[0][num_complete:num_complete+1]:
                list_of_incomplete_columns_through_output_plates.append(col)

    #print("\nlist_of_incomplete_columns_through_output_plates : ", list_of_incomplete_columns_through_output_plates)
    
    
    
    special_pick_up_tip_list = []
    
    for rack, num_complete_cols, num_wells_incomp_col in zip(tipracks, num_cols_completas, num_pocillos_col_incompleta):
        if num_wells_incomp_col != 0 : # There is an incomplete column in that rack
            special_pick_up_tip_list.append([subelement for element in rack.columns()[num_complete_cols:num_complete_cols+1] for subelement in element][8-num_wells_incomp_col])
    
        else: # All columns in that rack are complete columns
            special_pick_up_tip_list.append(None)
    
    #print("\nspecial_pick_up_tip_list : ", special_pick_up_tip_list)
    
    
    
    
    
    per_tip_pickup_current = .075 # 0.075 para p20 y 0.1 para p300
    
    for sample_col, output_col, num_incomplete_wells, tips in zip(list_of_incomplete_columns_through_sample_plates, list_of_incomplete_columns_through_output_plates, num_pocillos_col_incompleta, special_pick_up_tip_list):
        
        #print("\nsample_col : ", sample_col, " | output_col : ", output_col, " | num_incomplete_wells : ", num_incomplete_wells, " | tips : ", tips)
        
        if num_incomplete_wells != 0 and tips != None : # Si la columna está incompleta, entonces:
            # Definimos la cantidad de corriente que se va a usar para el pick up dependiendo de la cantidad de tips que se necesitan tomar
            pick_up_current = num_incomplete_wells*per_tip_pickup_current
            m20.pick_up_tip(tips)
            m20.aspirate(2, sample_col)
            m20.dispense(2, output_col)
            m20.touch_tip(v_offset=-0.5, speed=50)
            m20.drop_tip()
        
    

    
    
    # Transfering the Positive Controls from TubeRack to output_plates
    protocol.comment("\nPOSITIVE CONTROLS : ")
    for total_number_of_samples, plate in zip(sample_number, output_plates):
        s20.pick_up_tip()
        #s20.mix(20, 5, eppendorf_control_positivo)
        s20.aspirate(2, eppendorf_control_positivo)
        s20.touch_tip(v_offset=-0.5, speed=50)
        s20.dispense(s20.current_volume, plate.wells()[total_number_of_samples])
        s20.touch_tip(v_offset=-0.5, speed=50)
        s20.drop_tip()
    
    
    
    
    
    # Transfering the Negative Controls from TubeRack to output_plates
    protocol.comment("\nNEGATIVE CONTROLS : ")
    for total_number_of_samples, plate in zip(sample_number, output_plates):
        s20.pick_up_tip()
        #s20.mix(20, 5, eppendorf_control_positivo)
        s20.aspirate(2, eppendorf_control_negativo)
        s20.touch_tip(v_offset=-0.5, speed=50)
        s20.dispense(s20.current_volume, plate.wells()[total_number_of_samples+1])
        s20.touch_tip(v_offset=-0.5, speed=50)
        s20.drop_tip()