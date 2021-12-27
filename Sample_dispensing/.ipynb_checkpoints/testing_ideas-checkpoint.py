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
    _all_values = json.loads("""{"sample_number":[20, 40, 9],
    
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
    
    
    # NUMERO DE COLUMNAS COMPLETAS Y NUMERO DE POCILLOS CON MUESTRAS EN LA COLUMNA QUE QUEDA INCOMPLETA
    
    # Por 'num_cols_completas' sabemos el número de columnas completas que hay en cada placa.
    num_cols_completas = [divmod(number, 8)[0] for number in sample_number]
    print("\nnum_cols_completas : ", num_cols_completas)
    
    # Por 'num_pocillos_col_incompleta' sabemos cuantos pocillos de la columna incompleta tienen muestras, lo que nos permite tomar el número exacto de puntas necesarias.
    num_pocillos_col_incompleta = [divmod(number, 8)[1] for number in sample_number]
    #print("\nnum_pocillos_col_incompleta : ", num_pocillos_col_incompleta)
    
    

    
    
    # LISTA CON LAS COLUMNAS COMPLETAS EN CADA RACK
    
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
    
    
    
    lista_de_tips = []
    for rack, numero in zip(tipracks, num_cols_completas):
        lista_de_tips.append(rack.rows()[0][:numero])
    
    lista_de_tips = [subelement for element in lista_de_tips for subelement in element] # Make the previous list 'lista_de_puntas' a flat list
    

    
    #lista_de_tips = [tip_col for rack in tipracks for tip_col in [rack.rows()[0]][:num_cols_completas]]
    #print("\nlista_de_tips : ", lista_de_tips)
    
    
    for sample_col, output_col, tip_col in zip(list_of_complete_columns_through_sample_plates, list_of_complete_columns_through_output_plates, lista_de_tips):
        m20.pick_up_tip(tip_col)
        m20.aspirate(2, sample_col)
        m20.dispense(2, output_col)
        m20.drop_tip()