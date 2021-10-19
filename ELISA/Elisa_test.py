import math
import json
from opentrons import protocol_api, types
from opentrons.protocol_api.labware import Well

def get_values(*names):
    # Here you must change the values to meet your needs 
    _all_values = json.loads("""{"sample_number":96,"incubation_time":120,"washing_steps":6}""")
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
    
    
    # New class that can keep track its own volume
    class WellV(Well):
        
        def __init__(self, well, current_volume = 0):
            super().__init__(well._impl)
            self.well = well
            self.current_volume = current_volume
            
        def vol_dec(self, vol):
            if self.current_volume - vol > 0:
                self.current_volume = self.current_volume - vol
            else:
                self.current_volume = 0
            return(self.well)
        
        def vol_inc(self, vol):
            self.current_volume = self.current_volume + vol
            return(self.well)

    
    [sample_number, incubation_time, washing_steps] = get_values(
        "sample_number", "incubation_time", "washing_steps"
    )
    
    
    ## Labware
    # Defining the slots that bear the tips within the Opentron's deck
    total_tips = sample_number*8
    tiprack_num = math.ceil(total_tips/96)
    tip_slots = ['3', '6' , '9', '10'][:tiprack_num]
    
    # Defining the slots that bear the eppendorfs with stock samples within the Opentron's deck
    number_of_plates_with_stock_samples = math.ceil(sample_number/24)
    slots_of_plates_with_stock_samples = ['4','5','7','8'][:number_of_plates_with_stock_samples]
    
    # Loading tip racks
    tipracks = [protocol_context.load_labware_from_definition(Custom_Tiprack_DEF, slot) for slot in tip_slots]
    
    # Loading labware
    stock_plates = [protocol_context.load_labware('opentrons_24_tuberack_nest_1.5ml_snapcap', slot, 'original stock plate') for slot in slots_of_plates_with_stock_samples] 
    
    washing_plate = protocol_context.load_labware('usascientific_12_reservoir_22ml', '2', 'washing plate')
    test_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '1', 'test plate') # It must be the plate of the ELISA test (custom labware)
    
    
    # Defining the internal estructure of the washing plate
    ul_of_washing_buffer = 100*sample_number*washing_steps
    number_of_needed_wells = math.ceil(ul_of_washing_buffer/20) #20 is the max ammount of buffer that must be put on each well 
    PBST = [WellV(well, ul_of_washing_buffer) for well in washing_plate.rows()[0][:number_of_needed_wells]]
    #PBST = [WellV(wells, current_vol = ul_of_washing_buffer) for wells in washing_plate.wells()[:number_of_needed_wells]]
    # This is how it must be done by the hard way
    #PBST1 = washing_plate.wells[0]
    #PBST2 = washing_plate.wells[1]
    #PBST3 = washing_plate.wells[2]
    
    
    # Defining where the eppendorfs in the stock_plate are
    stock_col_num = math.ceil(sample_number/4)
    stock_samples = [well for well in stock_plates[0].wells()[:stock_col_num]]
    stock_output_single_channel = [well for well in test_plate.wells()[:stock_col_num]]
    
    
    # Defining where the wells in the test_plate are
    test_col_num = math.ceil(sample_number/8)
    test_samples = [WellV(col) for col in test_plate.rows()[0][:test_col_num]]
    
    
    
    # Instruments
    ## Loading instruments
    m300 = protocol_context.load_instrument('p300_multi_gen2', 'right', tip_racks=tipracks)
    s300 = protocol_context.load_instrument('p300_single_gen2', 'left', tip_racks=tipracks)
    
    ### Manipulating liquids at a lower rate (because of the tween)
    m300.flow_rate.aspirate = 40
    m300.flow_rate.dispense = 40
    m300.flow_rate.blow_out = 40
    
    
    
    # Commands
    ## First washing step: 100 uL of PBST to all samples to remove Coating step
    
      # New transfer function that use the functionalities of the above denifed class
    def transfer(vol, s:WellV, d:WellV, new_tip='never', pip=m300, blow_out=True, touch_tip=True):
        if new_tip=='never' and not pip.has_tip:
            pip.pick_up_tip()
        pip.transfer(vol, s.vol_dec(vol), d.vol_inc(vol), new_tip=new_tip, blow_out=blow_out, touch_tip=touch_tip)
    
    
    current_PBST_well = 0
    m300.pick_up_tip()
    for step in range(washing_steps):
        for sample in test_samples:
            if PBST[current_PBST_well].current_volume > 0:
                transfer(100, PBST[current_PBST_well], sample.top())
            
            else:
                current_PBST_well += 1
                transfer(100, PBST[current_PBST_well], sample.top())
                
            protocol_context.pause("Elimina el buffer que está en la placa con las muestras y luego apreta en 'resume' para continuar")
    m300.drop_tip()
    
    

    ## Transfering 100 uL of sample from each eppendorf of each stock plate to every well on the test_plate
    for stock_plate in stock_plates:
        for sample, output in zip(stock_samples, stock_output_single_channel):
            s300.mix(5, 150, sample)
            s300.transfer(100, sample, output, new_tip='always', touch_tip=True, blow_out=True)
    protocol_context.comment("Retirar la placa del Opentrons. Incubar en una caja humeda y a temperatura ambiente por 2:30:00 horas")
    
    
    