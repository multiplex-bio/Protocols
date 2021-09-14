from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'PCR protocol',
    'author': 'Multiplex',
    'description': 'First iteration. Primers: CVA, ACLSV, CNRMV',
    'apiLevel': '2.10'
}


def run(protocol: protocol_api.ProtocolContext):
    
    ## Labware
    # Tips
    tiprack_300 = protocol.load_labware('opentrons_96_tiprack_300ul', '9')
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', '6')
    
    # Wells
    reactives = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '8') 
    output = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '5')
    
    
    ## Instruments
    p300 = protocol.load_instrument('p300_single_gen2', 'left', tip_racks = [tiprack_300])
    p20 =  protocol.load_instrument('p20_single_gen2', 'right', tip_racks = [tiprack_20])
    
    
    ## Number of samples and Volumes are defined
    samples = 9
    
    # Volume Master mix
    MM = 25 # per well  
    MM_total_1to6 = 25 * 6 # Total to use
    MM_total_7to9 = 25 * 3
    
    
    # Volume DNA
    number_of_primers = 3
    DNA = 2.5
    DNA_total_1 = DNA*(samples/number_of_primers)
    DNA_total_2 = DNA*(samples/number_of_primers)
    
    
    # Volume H20
    H20_sample = 17.5 # 3 wells
    H20_ctrl = 20 # 3 wells
    H20_total = H20_sample*(6) + H20_ctrl*(3)
    
    # Volumes Primers
    LChv = 5
    LChv_total = LChv*(samples/number_of_primers)
    
    PNRSV = 5
    PNRSV_total = PNRSV*(samples/number_of_primers)
    
    PDV = 5
    PDV_total = PDV*(samples/number_of_primers)
    
    
    ## Commands
    ## Transporting reactives
    
    # Master Mix from reactives to output
    p300.pick_up_tip()
    p300.aspirate(MM_total_1to6, reactives['A1'])
    for i in range(6):
        p300.dispense(MM, output['A'+str(i+1)])
    p300.aspirate(MM_total_7to9, reactives['B1'])
    for i in range(3):
        p300.dispense(MM, output['A'+str(i+7)])
    p300.drop_tip()
    
    # H20 from reactives to output
    p300.pick_up_tip()
    p300.aspirate(H20_total, reactives['A2'])
    for i in range(samples):
        if (i+1) % 3 != 0: # Positivos
            p300.dispense(H20_sample, output['A'+str(i+1)])
        else: # Controls
            p300.dispense(H20_ctrl, output['A'+str(i+1)])
    p300.drop_tip()
    
    # LChv from reactives to output (just the ones in which it must be used)
    p20.pick_up_tip()
    p20.aspirate(LChv_total, reactives['A4'])
    for i in [3,2,1]: # First we dispense the primer within the negative control and then in the well with the sample
        p20.dispense(LChv, output['A'+str(i)])
    p20.drop_tip()
    
    # PNRSV
    p20.pick_up_tip()
    p20.aspirate(PNRSV_total, reactives['A5'])
    for i in [6,5,4]:
        p20.dispense(PNRSV, output['A'+str(i)])
    p20.drop_tip()
    
    #PDV
    p20.pick_up_tip()
    p20.aspirate(PDV_total, reactives['A6'])
    for i in [9,8,7]:
        p20.dispense(PDV, output['A'+str(i)])
    p20.drop_tip()
    
    # DNA from reactives to output (avoiding negative controls)
    for i in [1,4,7]:
        p20.pick_up_tip()
        p20.aspirate(DNA, reactives['A3'])
        p20.dispense(DNA, output['A'+str(i)])
        p20.drop_tip()
    
    for i in [2,5,8]:
        p20.pick_up_tip()
        p20.aspirate(DNA, reactives['B3'])
        p20.dispense(DNA, output['A'+str(i)])
        p20.drop_tip()