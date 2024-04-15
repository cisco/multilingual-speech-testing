# Speech Intelligibility Test (SIT)

- This script generates a qualtrics survey to subjetively measure the intelligibility of the speech. 


## Introduction:

- The survey is divided in 3 main parts:
    - `hearing test`: It is a special test used to measure the hearing capabilities of the participants.
    - `training test`: It is a set of specific files to train the participants of the survey; it is shown to the participants before the main test.
    - `main test`: It is the main test of the survey.

- To generate the speech intelligibility test we need the following datasets:

    - `hearing test`: The hearing test dataset contains 6 files used test the hearing abilities of the participants.
    - `training`: The training dataset has 2 categories: `clean` and`noisy`. It is used on train the participants of the survey before doing the main test.
    - `validation`: The validation dataset has 2 categories: `clean` and `noisy`. It is used as an anti-cheating mechanism on the main test.
    - `testing`: The testing dataset contains the files used in the main test.

### Input datasets structure:

- `hearing test`:

```
filename,target,resource_link
18S_093.wav,093,https://18S_093.wav
18S_193.wav,193,https://18S_193.wav
18S_293.wav,293,https://18S_293.wav

```

- `training`: 

```
filename,type,target,alternative1,resource_link
132.wav,clean,jilt,guilt, https://123.wav
133.wav,noisy,goal,coal, https://133.wav
133.wav,clean,floor,flower, https://133.wav
```

- `validation`:

```
filename,block,type,target,alternative1,resource_link
023.wav,1,noisy,myth,miss,https://023.wav
024.wav,1,clean,hot,hop,https://024.wav
025.wav,1,noisy,wroth,ross,https://025.wav
```

- `testing`:

```
filename,block,target,alternative1,resource_link
123.wav,1,myth,miss,https://123.wav
124.wav,1,hot,hop,https://124.wav
125.wav,1,wroth,ross,https://125.wav
```

- The training dataset is sampled according to the options (`survey_options`) of the survey.
- The validation dataset is sampled according to the options (`survey_options`) of the survey.
- The testing dataset includes files from the validation dataset based on the options (`survey_options`) of the survey.

## Project structure:

- `qualtrics_utils`: These are modules, utilities related to the qualtrics QSF file template.
    - `survey_components.py`: Helper function to access the components of the survey.
    - `survey_constants.py`: Constants of the QSF file. 
    - `survey_flow.py`: The QSF file contains a component called `Survey Flow`. This component has information of a FLOW inside the survey. It has helpers to access/manipulate the flow of the survey. 
    - `survey_metadata.py`: Helpers used to access the metadata of the survey.
    - `survey_payload_elements.py`: The payload elements are the elements of the component `Survey Blocks`. They contain the building blocks of the survey (same concept of block as in the web interface). This module has methods are particularly useful to access the content of an specific block.
    - `survey_questions.py`: This module has helpers to access and modify the current number of questions of the survey.

```python
qualtrics_utils
├── survey_components.py
├── survey_constants.py
├── survey_flow.py
├── survey_metadata.py
├── survey_payload_elements.py
└── survey_questions.py
```

- `templates`: Contains different packages and modules that are specific to the SIT project. 
    - The `baseline_qsf` folder contains the baseline QSF template
    - The `templates` folder contains different templates (JSON/python dictionaries) used in the survey: testing question template, training question template, block templates, among others.
    - The `template_helpers` folder contains modules to modify the templates in the `templates` folder.  

```python
│templates
│
├── baseline_qsf
│   ├── README.md
│   ├── SIT_prolific_mturk_unified_template.qsf
├── template_helpers
│   ├── README.md
│   ├── sit_blocks.py
│   └── sit_questions.py
└── templates
    ├── README.md
    └── block_templates.py
```

- `utils`: Contains general utilities to prepare the survey or to generate the survey. This involves basic methods and wrappers used in the main script `create_sit_test.py`.
    - `general.py`: Contains wrapper methods and utilities methods to set up the survey. 
    - `qsf_survey_preparation`: Contains methods that interact with the QSF to insert the blocks and questions.
    - `validation`: Contains validation methods for the json input configuration and input CSVs.

```python
│utils
├── general.py
├── qsf_survey_preparation.py
└── validation.py
```


## How to run a Survey

### Environment 

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

- `create_sit_test.py`: It is the main script to generate a survey, the input is a json file (`survey_config_example`).

### Execution

```
(env) python3 create_sit_test.py -ji examples/survey_recipe_release.json 
```


### Structure of the survey configuration file.

- The survey configuration file is as follows:

```json
{
    "survey_config": {
        "experiment_metafile": "experiment_survey_example.csv",
        "experiment_name": "experiment_name_1",
        "test_language": "spanish",
        "payment_rate": 0.0,
        "bonus": 0.0,
        "output_dir": "/output_folder/"
    },
    "survey_options": {
        "seed": 459361667,

        "hearing_test":{
            "hearing_test_metafile": "hearing_test_english_example.csv",
            "hearing_test_threshold": 13
        },
        "training": {
            "training_metafile": "experiment_training_example.csv",
            "clean": {
                "number_files": 8,
                "valid_expected": 6
            },
            "noisy": {
                "number_files": 8,
                "valid_expected": 6
            }
        },
        "validation": {
            "validation_metafile": "experiment_validation_example.csv",
            "clean": {
                "number_files": 0,
                "valid_expected": 0
            },
            "noisy": {
                "number_files": 20,
                "valid_expected": 15
            }
        }
    }
}

```

- It has 2 main keys: `survey_config` and `survey_options`
    - `survey_config` contains the settings related to the base configuration of the survey.
        - `experiment_metafile`: filepath of the testing metafile or experiment metafile.
        - `experiment_name`: name of the experiment. This name will be used to generate a unique hash for the survey.
        The testing files are dependent on the `test_language` key. 
       -  `test_language`: The default language of the qualtrics survey is english (EN). There is support for 6 additional languages: 
            - ES: Spanish. 
            - DE: German.
            - AR: Arabic.
            - JA: Japanese.
            - FR: French.
            - ZH-S: Chinese (Simplified).        
        - `payment_rate`: Expected hourly rate based on the duration of the survey.
        - `bonus`: Bonus payment value (rewarded for highest-quality submissions).
        - `output_dir`: This is the output directory of the files of the survey.  The output files will be saved in a folder inside the `output_dir`. The name of the folder is the survey hash (`SURVEY_HASH`). For example: `output_dir/a2f0edad511d9b4349bd4ca119593c21`.
    
    - `survey_options`: Contains the settings related to the configuration of the survey in terms of the stages: `hearing_test`, `training`, `validation`.
        - `hearing_test`: These are the settings for the hearing test.
            - `hearing_test_metafile`: filepath of the hearing test metafile.
            - `hearing_test_threshold`: threshold used to allow people to continue the survey. Min 0, Max 18.
          
        - `training`: These are the settings for the training data of the survey. 
            - `training_metafile`: filepath of the training metafile.

            - `clean`: `clean` is a type of training data, it is a category used in the training data. There are 2 options:
                - `number_files`: Indicates how many files of this category are needed in the training part of the survey. 
                - `valid_expected`: Indicates how many of them are expected to be correctly answered by the workers. 
            
            - `noisy`: `noisy` is a type of training data, it is a category used in the training data. There are 2 options:
                - `number_files`: Indicates how many files of this category are needed in the training part of the survey. 
                - `valid_expected`: Indicates how many of them are expected to be correctly answered by the workers. 

        - `validation`: these are the settings for the validation data of the survey. 
            - `validation_metafile`: filepath of the validation metafile.

            - `clean`: `clean` is a type of validation data, it is a category used in the training data. There are 2 options:
                - `number_files`: Indicates how many files of this category are needed in the training part of the survey. 
                - `valid_expected`: Indicates how many of them are expected to be correctly answered by the workers. 
            
            - `noisy`: `noisy` is a type of validation data, it is a category used in the training data. There are 2 options:
                - `number_files`: Indicates how many files of this category are needed in the training part of the survey. 
                - `valid_expected`: Indicates how many of them are expected to be correctly answered by the workers. 


## Survey structure:

- The main components of the survey are the `trainingBlock` and the `testingBlock`. 
    - `trainingBlock`: This block contains a set of files from the training dataset. They are sampled according to the `survey_options.training` options.
    - `testingBlock`: There are multiple testing blocks; they are built using validation and testing files based on the `survey_options.validation` options. 


