import math
import json
from opentrons import protocol_api, types
from opentrons.protocol_api.labware import Well

def get_values(*names):
    # Here you must change the values to meet your needs 
    _all_values = json.loads("""{"sample_number":14,"incubation_time":120,"washing_steps":3}""")
    return [_all_values[n] for n in names]

p200_TIPRACK_DEF_JSON = """{"ordering":[["A1","B1","C1","D1","E1","F1","G1","H1"],["A2","B2","C2","D2","E2","F2","G2","H2"],["A3","B3","C3","D3","E3","F3","G3","H3"],["A4","B4","C4","D4","E4","F4","G4","H4"],["A5","B5","C5","D5","E5","F5","G5","H5"],["A6","B6","C6","D6","E6","F6","G6","H6"],["A7","B7","C7","D7","E7","F7","G7","H7"],["A8","B8","C8","D8","E8","F8","G8","H8"],["A9","B9","C9","D9","E9","F9","G9","H9"],["A10","B10","C10","D10","E10","F10","G10","H10"],["A11","B11","C11","D11","E11","F11","G11","H11"],["A12","B12","C12","D12","E12","F12","G12","H12"]],"brand":{"brand":"Vertex","brandId":["4227-06"]},"metadata":{"displayName":"Vertex 96 Tip Rack 200 µL","displayCategory":"tipRack","displayVolumeUnits":"µL","tags":[]},"dimensions":{"xDimension":127.75,"yDimension":85.47,"zDimension":60.16},"wells":{"A1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":75.27,"z":9.35},"B1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":65.87,"z":9.35},"C1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":56.47,"z":9.35},"D1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":47.07,"z":9.35},"E1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":37.67,"z":9.35},"F1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":28.27,"z":9.35},"G1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":18.87,"z":9.35},"H1":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":14.85,"y":9.47,"z":9.35},"A2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":75.27,"z":9.35},"B2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":65.87,"z":9.35},"C2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":56.47,"z":9.35},"D2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":47.07,"z":9.35},"E2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":37.67,"z":9.35},"F2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":28.27,"z":9.35},"G2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":18.87,"z":9.35},"H2":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":23.75,"y":9.47,"z":9.35},"A3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":75.27,"z":9.35},"B3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":65.87,"z":9.35},"C3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":56.47,"z":9.35},"D3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":47.07,"z":9.35},"E3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":37.67,"z":9.35},"F3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":28.27,"z":9.35},"G3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":18.87,"z":9.35},"H3":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":32.65,"y":9.47,"z":9.35},"A4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":75.27,"z":9.35},"B4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":65.87,"z":9.35},"C4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":56.47,"z":9.35},"D4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":47.07,"z":9.35},"E4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":37.67,"z":9.35},"F4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":28.27,"z":9.35},"G4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":18.87,"z":9.35},"H4":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":41.55,"y":9.47,"z":9.35},"A5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":75.27,"z":9.35},"B5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":65.87,"z":9.35},"C5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":56.47,"z":9.35},"D5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":47.07,"z":9.35},"E5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":37.67,"z":9.35},"F5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":28.27,"z":9.35},"G5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":18.87,"z":9.35},"H5":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":50.45,"y":9.47,"z":9.35},"A6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":75.27,"z":9.35},"B6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":65.87,"z":9.35},"C6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":56.47,"z":9.35},"D6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":47.07,"z":9.35},"E6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":37.67,"z":9.35},"F6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":28.27,"z":9.35},"G6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":18.87,"z":9.35},"H6":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":59.35,"y":9.47,"z":9.35},"A7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":75.27,"z":9.35},"B7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":65.87,"z":9.35},"C7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":56.47,"z":9.35},"D7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":47.07,"z":9.35},"E7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":37.67,"z":9.35},"F7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":28.27,"z":9.35},"G7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":18.87,"z":9.35},"H7":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":68.25,"y":9.47,"z":9.35},"A8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":75.27,"z":9.35},"B8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":65.87,"z":9.35},"C8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":56.47,"z":9.35},"D8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":47.07,"z":9.35},"E8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":37.67,"z":9.35},"F8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":28.27,"z":9.35},"G8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":18.87,"z":9.35},"H8":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":77.15,"y":9.47,"z":9.35},"A9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":75.27,"z":9.35},"B9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":65.87,"z":9.35},"C9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":56.47,"z":9.35},"D9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":47.07,"z":9.35},"E9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":37.67,"z":9.35},"F9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":28.27,"z":9.35},"G9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":18.87,"z":9.35},"H9":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":86.05,"y":9.47,"z":9.35},"A10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":75.27,"z":9.35},"B10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":65.87,"z":9.35},"C10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":56.47,"z":9.35},"D10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":47.07,"z":9.35},"E10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":37.67,"z":9.35},"F10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":28.27,"z":9.35},"G10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":18.87,"z":9.35},"H10":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":94.95,"y":9.47,"z":9.35},"A11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":75.27,"z":9.35},"B11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":65.87,"z":9.35},"C11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":56.47,"z":9.35},"D11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":47.07,"z":9.35},"E11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":37.67,"z":9.35},"F11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":28.27,"z":9.35},"G11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":18.87,"z":9.35},"H11":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":103.85,"y":9.47,"z":9.35},"A12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":75.27,"z":9.35},"B12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":65.87,"z":9.35},"C12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":56.47,"z":9.35},"D12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":47.07,"z":9.35},"E12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":37.67,"z":9.35},"F12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":28.27,"z":9.35},"G12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":18.87,"z":9.35},"H12":{"depth":50.81,"totalLiquidVolume":200,"shape":"circular","diameter":5.77,"x":112.75,"y":9.47,"z":9.35}},"groups":[{"metadata":{},"wells":["A1","B1","C1","D1","E1","F1","G1","H1","A2","B2","C2","D2","E2","F2","G2","H2","A3","B3","C3","D3","E3","F3","G3","H3","A4","B4","C4","D4","E4","F4","G4","H4","A5","B5","C5","D5","E5","F5","G5","H5","A6","B6","C6","D6","E6","F6","G6","H6","A7","B7","C7","D7","E7","F7","G7","H7","A8","B8","C8","D8","E8","F8","G8","H8","A9","B9","C9","D9","E9","F9","G9","H9","A10","B10","C10","D10","E10","F10","G10","H10","A11","B11","C11","D11","E11","F11","G11","H11","A12","B12","C12","D12","E12","F12","G12","H12"]}],"parameters":{"format":"irregular","quirks":[],"isTiprack":true,"tipLength":50.81,"isMagneticModuleCompatible":false,"loadName":"vertex_96_tiprack_200ul"},"namespace":"custom_beta","version":1,"schemaVersion":2,"cornerOffsetFromSlot":{"x":0,"y":0,"z":0}}"""
Custom_Tiprack_DEF = json.loads(p200_TIPRACK_DEF_JSON)

metadata = {
    'protocolName': 'ELISA TEST',
    'author': 'Multiplex <bvalderrama@multiplex.bio>',
    'description': 'Elisa test protocol in Opentrons. Obs: The preparation of the buffers must be done before this protocol',
    'source': 'Modified from Protocol Library',
    'apiLevel': '2.11'
    }


def run(protocol_context):

    
    [sample_number, incubation_time, washing_steps] = get_values(
        "sample_number", "incubation_time", "washing_steps"
    )
    
    
    ## Labware
    # Defining the slots that bear the tips within the Opentron's deck
    total_tips = sample_number*8
    tiprack_num = math.ceil(total_tips/96)
    tip_slots = ['3', '6' , '9', '10'][:tiprack_num]
    
    
    # Loading tip racks
    tipracks = [protocol_context.load_labware_from_definition(Custom_Tiprack_DEF, slot) for slot in tip_slots]
    
    
    ## Instruments
    # Loading instruments: Single and Multi-channel 300uL pipettes
    m300 = protocol_context.load_instrument('p300_multi_gen2', 'right', tip_racks=tipracks)
    s300 = protocol_context.load_instrument('p300_single_gen2', 'left', tip_racks=tipracks)
    
    
    ## LABWARE:
    
    # Reservoir con washing buffer
    washing_reservoir = protocol_context.load_labware('usascientific_12_reservoir_22ml', '2', 'Washing reservoir')
    
    # Defining the internal structure of the washing plate ## || Pensar si se puede hacer este mismo diccionario con un for loop que itere tantas veces como washing steps haya
    PBST_dic = { # Cada uno debe tener 20 mL de washing buffer, que es suficiente para que cada uno tenga buffer para lavar 96 wells con 200 uL
        'PBST1' : washing_reservoir.wells()[0],
        'PBST2' : washing_reservoir.wells()[1],
        'PBST3' : washing_reservoir.wells()[2],
    }
    
    
    # EL PLATE DONDE SE REALIZA EL TEST DE ELISA
    # Loading labware: ELISA plate -> Plate where the ELISA test is conducted. It is a custom labware
    elisa_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '1', 'Elisa test plate') # It must be the plate of the ELISA test (custom labware)
    
    elisa_plate_number_of_cols = math.ceil(sample_number/8)
    elisa_samples = [col for col in elisa_plate.rows()[0][:elisa_plate_number_of_cols]]
    
    
    ### Manipulating liquids at a lower rate (because of the tween)
    m300.flow_rate.aspirate = 40
    m300.flow_rate.dispense = 40
    m300.flow_rate.blow_out = 40
    
    
    
    

    # FOURTH STEP: CONJUGATE REAGENT
    #' Si son 24 muestras o menos, hacerlo con la single channel
    
    # Se carga el washing reservoir con 3 carriles con washing buffer y un slot con el conjugate buffer
    conjugate_reagent = washing_reservoir.wells()[5]
    
    
    # Transfering 200 uL of Conjugate Reagent to the ELISA test wells
    m300.pick_up_tip()
    for sample in elisa_samples:
        m300.transfer(200, conjugate_reagent, sample.top(), new_tip='never', touch_tip=True, blow_out=True)
    m300.drop_tip()
    
    
    # Incubation step
    protocol_context.comment("Retirar la placa. Incubar por 2:00:00 horas a 37°C")
    
    
    # Washing: Removing the Conjugate reagent with washing buffer
    m300.pick_up_tip()
    for key, washing_buffer in PBST_dic.items():
        for sample in elisa_samples:
            m300.transfer(200, washing_buffer, sample.top(), touch_tip=True, blow_out=True, new_tip='never')
        protocol_context.delay(minutes=3, msg='3 minutes incubation')
        protocol_context.pause("Descarta el buffer sobre un paño, coloca la placa de nuevo en el robot y apreta 'resume' para continuar")
    m300.drop_tip()