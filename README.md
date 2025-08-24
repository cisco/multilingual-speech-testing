# Multilingual Speech Testing

This repository is a collection of real-world speech recordings and tools to facilitate subjective testing and analysis. The datasets are designed for speech quality and intellgibility assessment purposes, including subjective tests in laboratory or crowdsourced settings.

## Speech Intelligibility Assessment

We provide [audio files](speech-intelligibility-DRT/) and [support code](survey-setup-tools/survey-generation/DRT) for the Diagnostic Rhyme Test (DRT) to assess speech intelligibility in several languages.

## Crowdsourced MUSHRA Testing

We share [helper code](survey-setup-tools/survey-generation/MUSHRA/) to set up crowdsourced MUSHRA tests. The test design and participant screening follows ITU recommendations and has been adapted to the crowdsourced setting. The flexible test setup can be performed with any suitable high-quality clean speech test data. The tool is an implementation of the test approach described in our paper ["Crowdsourcing MUSHRA Tests in the Age of Generative Speech Technologies: A Comparative Analysis of Subjective and Objective Testing Methods"](https://www.isca-archive.org/interspeech_2025/lechler25_interspeech.html) presented at INTERSPEECH 2025 in Rotterdam. 

## Low-Resource Audio Codec (LRAC) Challenge Test Data

This repo hosts the test data for the [Low-Resource Audio Codec (LRAC) Challenge 2025](https://crowdsourcing.cisco.com/lrac-challenge/2025/). The open test sets for both challenge tracks have been released now and each contain clean speech as well as reverberant and noisy test folders with respective clean references. Please consult the [open test set description](https://crowdsourcing.cisco.com/lrac-challenge/2025/evaluation#objective-evaluation) for further details. The open test sets are designed specifically for evaluation with objective metrics. 
In the final test phase, we will also release blind testing materials for human listening tests, which will be used to determine the challenge winner. These test sets contain predominantly real-world recordings. Please check the [evaluation plan](https://crowdsourcing.cisco.com/lrac-challenge/2025/evaluation#subjective-evaluation) for further details. The blind test sets will be released on September 30, 2025. 

## Acknowledgements

We are extremely greatful for the extensive support that our colleagues and collaborators have provided in the realisation of these multilingual speech testing resources. Specifically, we would like to thank Nerio Morán Páez, Miguel Plaza Rosillon, Tarek Afifi, Ginette Leon Prato, Daniel Arismendi, Shirley Pestana Rodriguez, Omid Roshani, Jose Kordahi, Cyprian Wronka, Anna Bartlett, and Ana Rivera Jaramillo. We appreciate their meticulous attention to detail and relentless dedication that was essential to getting this project off the ground.

# Licensing

Unless stated otherwise, these multilingual speech datasets are licensed under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
