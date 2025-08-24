# MUSHRA: Multiple Stimuli with Hidden Reference and Anchor

- This script prepares the subjective test for Multiple Stimuli with Hidden Reference and Anchor (MUSHRA) tests.
- The result is a .qsf file which can be uploaded to Qualtrics to generate a survey.
- Once published, the link to this survey can be inserted into a SIT_DRT package config file to be uploaded to Survey App. 


## Introduction:

- The MUSHRA survey assumes the use of one dataset (any clean speech set) and several test conditions (we recommend testing a maximum of 4 systems plus reference and anchor):
    - `testing_metafile`: The testing metafiles contains a column that index all the files that required to be tested.
    - The `target_filename_column`, indicates the column that will be used to get the all the names of the files of the experiment.
    - These names will be used to find the the files on every condition, if the one of the files is not present in the conditions,
    the experiment will raise an alert and it will not generate the survey.
    - The `conditions` are different representations of the same files. i.e: ref, opus_1kbps, opus_3kbps, opus_6kbps, opus_9kbps, opus_12kbps.


## Project structure:

- `qualtrics_utils`: These are modules, utilities related to work with the qualtrics QSF file template.


- `MUSHRA`: Contains different packages and modules that are specific for the MIP project. 
    - The `baseline_qsf` folder contains the baseline QSF template for the MIP survey.
    - The `survey` folder contains a module to prepare the survey, sampling, generate questions, update the QSF file, among others.
    - The `templates` folder contains different templates (JSON/python dictionaries) used in the survey: testing question template, block templates, among others.
    - The `template_helpers` are contains modules to modify the templates in the `templates` folder.  
    - The validation helpers in`utils` are modules to make sure the input in of the survey is correct. 

```bash
MUSHRA/
|-- README.md
|-- __init__.py
|-- baseline_qsf
|   |-- mushra_survey.qsf
|-- examples
|   |-- mushra_recipe_release.json
|   |-- testing_metafile_example.csv
|-- qualtrics_utils
|   |-- README.md
|   |-- __init__.py
|   |-- survey_components.py
|   |-- survey_constants.py
|   |-- survey_flow.py
|   |-- survey_metadata.py
|   |-- survey_payload_elements.py
|   |-- survey_questions.py
|-- survey
|   |-- data_preparation.py
|   |-- survey_preparation.py
|-- template_helpers
|   |-- mushra_blocks.py
|   |-- mushra_questions.py
|-- templates
|   |-- block_templates.py
|-- utils
    |-- validation.py
```

## How to run a Survey

- `create_mushra_test.py`: It is the main script to generate a survey, the input is a json file (`survey_config_example`).

```python
(env) python create_mushra_test.py -ji examples/mushra_recipe_release.json
```

### Structure of the survey configuration file.

The survey configuration file has two main keys: `survey_config` and `survey_options`
    - `survey_config` contains the settings related to the creation of the survey.
        - `experiment_name`: name of the experiment. This name will be used to generate a unique hash for the survey.
        - `testing_metafile`: This is the location of the testing CSV that contains the information of the testing files. It can have any format, but it should contain the column in `target_filename_column`.
        - `target_filename_column`: This is the column in the `testing_metafile` that will be used to find the files in the `conditions`.
        - `output_dir`: This is the output directory of the files of the survey. The output files will be saved in a folder inside the `output_dir`. 
            - It follows this format: `output_dir/experiment_name/5db72aafab9d67972a670b4b8deb81fb/`. The output directory will have the following files:
            - `meta_survey.csv`: It is a copy of the testing metafile, with new columns containing indexing the hash files.
            - `survey_generation.log`: Log of the generation of the survey.
            - `survery_qualtrics_SURVEY_HASH.qsf`: Generated QSF file. Used to upload the survey to the qualtrics platform.
            - `survey_recipe.json`: This is the recipe to generate the same survey again. It can be used to replicate exactly the same output.
        - `pay_region`: The pay region is a configuration located in internal utils that defines the approximate payment rate and the bonus 1, bonus 2 and bonus 3 values in USD. (see Internal Configuration)
        - `overwrite`: If the experiment name key is repeated (`experiment_name`) the script will stop. To avoid to overwrite the survey in the s3, use `overwrite:false`.
    - `survey_options`: Contains the settings related to the validation files.
        - `seed`: The seed is used to replicate experiments.
        - `survey_question`: Question used in the header of each question of the survey.
        - `training`: The training section allows the use of controlled example files for listener training. 
        - `training_attemps_limit`:In the training section, users are allowed multiple attempts to score a question. The `training_attempts_limit` specifies the maximum number of attempts permitted per question. Once a user reaches this limit, the next question will be loaded.

        - `training_pass_threshold`: The training section is designed to instruct users on accurately rating conditions within the rating job. Additionally, it serves as a means to identify users who comprehend the task. The `training_pass_threshold` represents the maximum number of attempts a user can make in the dynamic training section without incurring penalties, such as restrictions on taking multiple rating jobs.

        - `blocks`: The questions of the survey are divided in blocks. Each block has N questions. It is delegated to the researcher how many blocks or (an only or) how
        many questions per block it is required. When none of them is specified, by default, the number of questions per block will be the maximum without reaching out 25 audio files in total.
        For example, if the question has 6 conditions (6 audio files), each block will have up to 4 questions or 6*4 =24 audio files.

        - `ref_threshold`: The reference threshold represents the minimum value a reference file should have in order to be considered correct. A reference file with a score lower than `ref_threshold` is considered an incorrect annotation.
        - `anchor_threshold`: The anchor threshold represents the maximum value a anchor file should have in order to be considered correct. An anchor file with score highger than `anchor_threshold` is considered an incorrect annotation.
        - `anchor_min_distance_wrt_reference`: The anchor min distance with respect to the reference represents the minimium distance between the reference and the anchor in order to be considered
        correct. This based on the assumption that the distance between the anchor and reference should be big enough. For example, for a anchor min distance of 30 points:
            - User score reference as 100, the threshold for the anchor is `100-30 = 70`, if the anchor is above 70, it is considered an irregularity. 
            - User score reference as 90, the threshold for the anchor is `90-30 = 60`, if the anchor is above 60, it is considered an irregularity. 
            - User score reference as 50, the threshold for the anchor is `50-30 = 20`, if the anchor is above 20, it is considered an irregularity.
        - `correct_answers_threshold`: This is a threshold for correct answers. In a given block a user answers N questions. This threshold makes reference to how many questions from the block were correctly answered in terms of the anchor and the reference thresholds. This threshold is used to allow good surveyors to get an additional block with more questions. When surveyors fail in answering the anchor and reference of the question, the survey is finished. 
        - `conditions`: List of dictionaries containing the `name` and `path` of all the conditions to test.
            - `name` is the name of the condition. 
            - `path` is the path to the folder containing the files of the condition. The files in this folder must match the filenames in the `testing_metafile`.

> **NOTE: it is mandatory to incude the condition with name `ref`. This experiment makes the assumption that this set of files exists**.

> **NOTE: it is mandatory to incude the condition with name `anchor`. This experiment makes the assumption that this set of files exists**.

> **NOTE: The `anchor_threshold` and `anchor_min_distance_wrt_reference` can not be defined at the same time, one of them has to be null. Both conditions can not be applied in the rating job**.


## Survey structure:

- The main components of the survey are the `introduction` and the `testingBlock`. 
    - `introduction`: This block contains instructions about the survey and examples of how to complete the survey.
    - `hearing test`: This block makes sure the user can participate in the survey.
    - `trainig`: This block makes sure the user understand the survey. It has an example of the rating job.
    - `testingBlock`: There are multiple testing blocks, each block contains a set of questions based on the configuration provided.
    - `extra test`: This block appears when the surveyor is responding correctly the questions in terms of the anchor and reference.


