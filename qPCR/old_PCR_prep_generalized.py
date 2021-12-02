## Inventory of issues: 
# - Calculate the total tips needed for the protocol when using single channel pipettes
# - 

from opentrons.protocol_api import ProtocolContext
import math

# metadata
metadata = {
    'protocolName': 'Mixing PCR reagents: Protocol to mix MasterMix and DNA from up to 96 samples.',
    'author': 'Multiplex',
    'description': ' All samples must use the same type primers. To prepare PCR mix with different kind of primers a novel protocol must be coded. See PCR_Sep* for details',
    'apiLevel': '2.10'
}


pipette_type = 'p20_multi_gen2'
pipette_mount = 'left'
sample_number = 96
MasterMix_volume = 48 #uL
DNA_volume = 2 #uL


def run(protocol_context: ProtocolContext):
        
    # Labware
    ## Wells
    MasterMix_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '1', 'Master Mix plate')
    output_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '4')
    samples_plate = protocol_context.load_labware('biorad_96_wellplate_200ul_pcr', '2', 'DNA plate')
    
    ### List of wells with samples
    num_columns = math.ceil(sample_number/8)
    samples = samples_plate.rows()[0][:num_columns]
    reagents = MasterMix_plate.rows()[0][:num_columns]
    outputs = output_plate.rows()[0][:num_columns]
    
    
    ## Tips
    tiprack1 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul','3', 'Tip Box 1') 
    tiprack2 = protocol_context.load_labware('opentrons_96_filtertiprack_20ul','6', 'Tip Box 2') 
    
    
    # Instruments
    m20 =  protocol_context.load_instrument(pipette_type, pipette_mount, tip_racks = [tiprack1, tiprack2])
       
    
    # Commands
    ## Adding MasterMix from MasterMix_plate to the output_plate
    m20.pick_up_tip()
    for reagent, output  in zip(reagents, outputs):
        m20.transfer(MasterMix_volume, reagent, output, new_tip='never', blow_out=True)
    m20.drop_tip()
    
    
    ## Adding DNA from samples_plate to the output_plate
    for sample, output, tip in zip(reagents, outputs, tiprack2.rows()[0][:num_columns]):
        m20.pick_up_tip()
        m20.transfer(DNA_volume, sample, output.bottom(), new_tip='never', blow_out=True, touch_tip=True)
        m20.drop_tip()