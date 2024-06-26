# Speech Intelligibility Test (SIT): survey generation and results analysis

This repository contains scripts to generate a SIT survey through Qualtrics and to analyze the results. These scripts are developed to accompany the release of multilingual Diagnostic Rhyme Test (DRT) audio data: for details, see the corresponding [repository]().

The project has two main components: [survey_generation](survey_generation) and [results_analysis](results_analysis).


## Generate a survey
A Qualtrics qsf file is generated by running this script, with a json file as input:

### Environment 

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Execution

```
(env) python3 create_sit_test.py -ji examples/survey_recipe_release.json 
```

This qsf file can then be uploaded to Qualtrics to run the SIT test.

These files are contained in the `survey_generation` directory. For details, refer to the corresponding [documentation](survey_generation/README.md).


## Analyze survey results
The `results_analysis` [directory](results_analysis) is under construction. It will contain tools to analyze test results collected through Qualtrics.


## Structure of SIT Survey
This SIT survey is based on the DRT format and consists of the following blocks:
![Visual representation of SIT survey blocks](https://github.com/BabbleLabs/subjective_intelligibility_test_software_release/blob/master/survey-setup-tools/wiki/survey_flowchart.png)

For a more detailed outline of the survey components and specifications, please refer to the project [wiki](https://github.com/BabbleLabs/subjective_intelligibility_test_software_release/wiki/Qualtrics-SIT-Survey).


## Requirements

### Data
This SIT survey is based on multilingual DRT datasets. The present scripts assume specfic data formatting requirements. For these dataset specifications, please refer to `survey_generation` [documentation](survey_generation/README.md).

### Qualtrics
The use of this Qualtrics qsf file requires a Qualtrics paid account, as crucial features used in the test are not supported by free accounts.


## CONTRIBUTION

[CONTRIBUTING.md](CONTRIBUTING.md)

## LICENSE

[LICENSE](LICENSE)
