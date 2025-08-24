"""
Cisco Systems, Inc. and its affiliates
"""
"""
MUSHRA blocks helpers
"""

import copy
import random, string

from templates.block_templates import (
    BLOCK_TEMPLATE,
    DYNAMIC_TRAINING_BLOCK_TEMPLATE,
    FLOW_BLOCK_TEMPLATE,
    FLOW_BLOCK_RANDOMIZER_ITEM,
    FLOW_DYNAMIC_TRAINING_BLOCK_TEMPLATE,
    FLOW_BLOCK_DYNAMIC_TRAINING_RANDOMIZER_ITEM,
    HEARING_TEST_TEMPLATE,
)


def generate_qualtrics_block_id():
    """Generate block ID.
    This generates a block ID as in qualtrics. BL_ + 15 digits
    """
    BLOCK_ID_BASE = "BL_"

    return BLOCK_ID_BASE + "".join(
        random.choices(string.ascii_letters + string.digits, k=15)
    )


def create_new_testing_block(block_id, block_name):
    """Create new testing qualtrics block.
    This is a new testing block (qualtrics block)

    Args:
        block_id(str): block id. Generated with `generate_qualtrics_block_id()`
        block_name(str): block desriptive name.

    Return:
        new block template.
    """

    description_placeholder = "DESCRIPTION_ID_PLACEHOLDER"
    block_id_plaholder = "DESCRIPTION_ID_PLACEHOLDER"

    block_template = copy.deepcopy(BLOCK_TEMPLATE)

    block_template["ID"] = block_id
    block_template["Description"] = block_name
    block_template["BlockElements"] = []

    return block_template


def create_new_flow_block(flow_id, block_id_index_map, current_max_flow_id):
    """Create a new block flow with a list of block items.
    The flow block is standard for the testing block. It is BlockRandomizer and it references
    all the testing blocks. The ID of the block is needed with the payload index that is used to indicate create a FlowID.
    {block_id:'N'}.

    Each question is randomized
    Args:
        flow_id (str): Flow ID in the survey data.
        block_id_index_map(dict): Mapping of block_id->payload index mapping dictionary.
        current_max_flow_id(int): current max flow index (not already existing)
    """
    BLOCK_N_SELECTED_PLACEHOLDER = "BLOCK_N_SELECTED"
    BLOCK_ID_PLACEHOLDER = "BLOCK_ID"
    # Flow randomizer template
    flow_block_template = copy.deepcopy(FLOW_BLOCK_TEMPLATE)
    flow_block_template["FlowID"] = flow_id
    current_max_flow_id += 1

    # generate the list of references
    reference_block_list = []
    for block_id, payload_index_block_number in block_id_index_map.items():
        # Survey block number
        block_number = payload_index_block_number[1]

        # Create new template.
        current_template_item = copy.deepcopy(FLOW_BLOCK_RANDOMIZER_ITEM)

        # Update flow id for flow randomizer item
        current_flow_id = "FL_" + str(current_max_flow_id)
        current_template_item["FlowID"] = current_flow_id
        current_max_flow_id += 1

        # Update branch logic (Left operand embedded variable)
        block_selected_template = "block_{}_selected".format(block_number)
        current_template_item["BranchLogic"]["0"]["0"][
            "LeftOperand"
        ] = block_selected_template

        # Update branch logic (Description)
        description = current_template_item["BranchLogic"]["0"]["0"]["Description"]
        current_template_item["BranchLogic"]["0"]["0"][
            "Description"
        ] = description.replace(BLOCK_N_SELECTED_PLACEHOLDER, block_selected_template)

        # For each element in the internal flow, update flow ID
        for index in range(0, len(current_template_item["Flow"])):
            current_flow_id = "FL_" + str(current_max_flow_id)
            current_template_item["Flow"][index]["FlowID"] = current_flow_id

            # Update current block
            if "ID" in current_template_item["Flow"][index].keys():
                if current_template_item["Flow"][index]["ID"] == BLOCK_ID_PLACEHOLDER:
                    current_template_item["Flow"][index]["ID"] = block_id

            # Update selected block condition
            if "EmbeddedData" in current_template_item["Flow"][index].keys():
                for index_embedded_data in range(
                    0, len(current_template_item["Flow"][index]["EmbeddedData"])
                ):
                    description = current_template_item["Flow"][index]["EmbeddedData"][
                        index_embedded_data
                    ]["Description"]

                    if description == BLOCK_N_SELECTED_PLACEHOLDER:
                        current_template_item["Flow"][index]["EmbeddedData"][
                            index_embedded_data
                        ]["Description"] = block_selected_template
                        current_template_item["Flow"][index]["EmbeddedData"][
                            index_embedded_data
                        ]["Field"] = block_selected_template

            current_max_flow_id += 1

        reference_block_list.append(current_template_item)

    # assign reference list to flow template
    flow_block_template["Flow"] = reference_block_list

    return flow_block_template


def create_new_dynamic_training_block(block_id, block_name):
    """Create new qualtrics block for the dynamic training.
    This is a new dynamic training block (qualtrics block)

    Args:
        block_id(str): block id. Generated with `generate_qualtrics_block_id()`
        block_name(str): block desriptive name.

    Return:
        new block template.
    """
    description_placeholder = "DESCRIPTION_ID_PLACEHOLDER"
    block_id_plaholder = "DESCRIPTION_ID_PLACEHOLDER"

    block_template = copy.deepcopy(DYNAMIC_TRAINING_BLOCK_TEMPLATE)

    block_template["ID"] = block_id
    block_template["Description"] = block_name
    block_template["BlockElements"] = []

    return block_template


def create_new_dynamic_training_flow_block(
    flow_id, block_id_index_map, current_max_flow_id, subset
):
    """Create a new block flow with a list of block items.
    The flow block is standard for the training block. It is BlockRandomizer and it references
    all the training blocks. The ID of the block is needed with the payload index that is used to indicate create a FlowID.
    {block_id:'N'}.

    Each question is randomized
    Args:
        flow_id (str): Flow ID in the survey data.
        block_id_index_map(dict): Mapping of block_id->payload index mapping dictionary.
        current_max_flow_id(int): current max flow index (not already existing).
        subset: Number of question to show in the randomizer.
    """

    # Flow randomizer template
    flow_block_template = copy.deepcopy(FLOW_DYNAMIC_TRAINING_BLOCK_TEMPLATE)
    flow_block_template["FlowID"] = flow_id
    flow_block_template["SubSet"] = subset
    current_max_flow_id += 1

    # generate the list of references
    reference_block_list = []
    for block_id, payload_index_block_number in block_id_index_map.items():
        # Create new flow item template.
        current_template_item = copy.deepcopy(
            FLOW_BLOCK_DYNAMIC_TRAINING_RANDOMIZER_ITEM
        )

        # Update flow id for flow randomizer item
        current_flow_id = "FL_" + str(current_max_flow_id)
        current_template_item["FlowID"] = current_flow_id
        current_template_item["ID"] = block_id
        current_max_flow_id += 1

        reference_block_list.append(current_template_item)

    # assign reference list to flow template
    flow_block_template["Flow"] = reference_block_list

    return flow_block_template


def create_hearing_test_block(hearing_test_options):
    """create a new survey hearing test block.
    Update the audio links for the hearing test based on the hearing_test_options
    Args:
        survey_data (JSON): Survey QSF data.
        hearing_test_options(dict): {option: link, digits}.
    Return:
        survey_data (JSON): Updated Survey.
    """
    # load hearing test template
    hearing_test_template = copy.deepcopy(HEARING_TEST_TEMPLATE)

    # change hearing options on default language
    for key in hearing_test_options.keys():
        hearing_test_template["Payload"]["Answers"][key][
            "Display"
        ] = hearing_test_template["Payload"]["Answers"][key]["Display"].replace(
            "AUDIO_LINK_PLACEHOLDER", hearing_test_options[key][0]
        )

    return hearing_test_template
