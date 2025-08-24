# qualtrics utils

- General qualtrics utilities. These are utilities related to QSF file from qualtrics.
- Common and general utilities that are part of the QSF file of qualtrics and they are not bind to any specific survey.


## Modules:

- The following modules contains helper functions to work with the QSF file.
- TODO: Wiki description  of QSF qualtrics structure.

### survey_components.py

- The QSF file is composed of elements. It element is associated with an index inside the QSF.
- Some of these elements are:
    - `Survey Blocks`: Contains the building blocks of the survey (same concept of block as in the web interface).
    - `Survey Flow`: This contains structure of the flow of the survey. All the blocks of the survey are part of a survey.
    - `Survey Question Count`: The number of questions of the survey.
    - `QID_XXXX`: It is a question component. The blocks are composed of questions.

- Helper functions to access the components of the survey.
    - `get_survey_component_index_map`
    - `get_number_of_survey_components`


### survey_flow.py

- The QSF file contains a component called `Survey Flow`. This component has information of a FLOW inside the survey. It has also has information about the blocks that are part of the flow. 

- Helper functions to access the components of the survey.
    - `get_current_number_of_flow_ids`
    - `update_survey_number_of_flow_ids`
    - `get_survey_flow_index_map`
    - `get_survey_flow_index_by_block_id`
    - `update_flow_by_payload_index`


### survey_payload_elements.py

- The payload elements are the elements of the component `Survey Blocks`. They contains the building blocks of the survey (same concept of block as in the web interface). These methods are particularly useful to access the content of an specific block.

- Helper functions to access the components of the survey.
    - `get_survey_block_element_payload_map`
    - `get_last_survey_block_element_payload`
    - `add_new_survey_block_element_payload`
    - `insert_new_survey_block_element_payload`



### survey_questions.py

- These module has helpers to access and modify the current number of questions of the survey.
- The survey component `Survey Question Count` contains this information and it is used as counter to define the ID's of the questions. In other word, the number of questions define the ID of a new question.
- When question is created in the survey, it exists in 2 parts: **The survey components** where the definition and details of the question exist and the in **payload elements** where the blocks of the survey refer to them.

- Helper functions to access the components of the survey.
    - `get_current_number_of_questions`
    - `update_survey_number_of_questions`
    - `insert_question_referecences_on_block`