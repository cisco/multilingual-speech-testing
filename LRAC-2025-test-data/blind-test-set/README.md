# Blind Test Sets for the LRAC 2025 Challenge

This folder contains the blind test sets for both challenge tracks of the LRAC Challenge 2025. 
Details of these subjective evaluation sets can be found on the [Challenge Website](https://crowdsourcing.cisco.com/lrac-challenge/2025/evaluation#subjective-evaluation). 

## Folder structure
In line with the evaluation procedure of the LRAC Challenge 2025, the files are separated by track and test case, as described on the [Challenge Website](https://crowdsourcing.cisco.com/lrac-challenge/2025/evaluation#subjective-evaluation). Note that the "clean" and "drt_en_clean" subsets are the same for both tracks.

|-- track_1
|   |-- clean
|   |-- drt_en_clean
|   |-- realworld
|   `-- simultaneous_talkers
`-- track_2
    |-- clean
    |-- drt_en_clean
    |-- drt_en_noisy
    |-- noisy
    `-- reverberant

## Notes on the use of this data
All test data of the blind test sets is suitable for the purpose of evaluating codecs and possibly other speech processing applications in human listening tests beyond the scope of this challenge. 

The source licenses for the blind test set audio data are suitable for research and development as well as commercial use (subject to further obligations of attribution and share-alike responsibilities in many cases). Please see individual CSV files with meta data for file-specific source and license information. 

The majority of the audio data is original audio data collected by Cisco Systems and hereby open-sourced for the benefit of the speech and signal processing community under [CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).
Other sources of data are listed below with the respective general license for each data set. File-specific license information can be found in the meta.csv files inside the subset folders. 

## Data sources
- Original audio data collected by Cisco Systems via crowdsourcing on Prolific, Amazon Mechanical Turk, and Upwork and hereby open-sourced for the benefit of the speech and signal processing community under CC BY-SA 4.0 license (https://github.com/cisco/multilingual-speech-testing/blob/main/LICENSE.txt)
- L. Lechler, K. Wojcicki, "Crowdsourced Multilingual Speech Intelligibility Testing," in ICASSP, 2024, pp. 1441-1445.The Diagnostic Rhyme Test data in this test set is a subset of the English data set previously released in this [repository](https://github.com/cisco/multilingual-speech-testing/tree/main/speech-intelligibility-DRT/data-16kHz/English) but at a sampling rate of 24 kHz. This data is licensed under CC BY-SA 4.0 license (https://github.com/cisco/multilingual-speech-testing/blob/main/LICENSE.txt). The 'drt_en_noisy' subset was augmented with speech-shaped noise at an SNR of 5 dB. 
- Demirsahin, I., et al, "Open-source Multi-speaker Corpora of the English Accents in the British Isles," in Proceedings of The 12th Language Resources and Evaluation Conference (LREC), 2020, pp. 6532–6541. Accessed via Open SLR [SLR83](https://www.openslr.org/83/) published under [CC BY-SA 4.0 license](https://openslr.trmal.net/resources/83/LICENSE). 
- [SoundCloud](https://soundcloud.com/) under appropriate license (any files used were marked with [CC BY license](https://creativecommons.org/licenses/by/4.0/))
- [Wikimedia audio resources](https://commons.wikimedia.org/wiki/Category:Audio_files) under appropriate license (any files used were marked with [CC BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/3.0/deed.en))

Any files may have been modified from the original in terms of the duration of the audio file (cropping) as well as level rescaling. Additional meta data may have been provided that may not stem from the original source but was either labelled by human annotators or generated using [OpenAI's Whisper](https://github.com/openai/whisper), open-sourced under [MIT license](https://github.com/openai/whisper/blob/main/LICENSE) for ASR, language identification, accent identification, and speaker gender prediction, if not available at the source. Pitch was estimated using [YYAPT](https://github.com/bjbschmitt/AMFM_decompy), also open-sourced under [MIT license](https://github.com/bjbschmitt/AMFM_decompy/blob/master/LICENSE). 