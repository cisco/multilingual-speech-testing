# Testing Speech Intelligibility with the Multilingual Diagnostic Rhyme Test

This repository contains audio recordings and information on the diagnostic rhyme test (DRT) in several languages.
Further details about the data, test procedure, and initial test results obtained with this data can be found in our paper [[1]](#bibliography).

## Language Versions of the Diagnostic Rhyme Test

At present, speech recordings for six datasets in five languages are available here. We plan to extend this list in the future.

### Chinese (Mandarin) Consonant Contrast
The Mandarin Chinese DRT was recorded without modification of the word list [[2]](#bibliography). Both simplified Chinese and pinyin transcriptions were used to elicit the correct pronunciation in
the recording sessions. We recommend to also present both to participants at test time. The test list contains 96 word pairs (192 unique words).
The six distinctive features for Chinese are _airflow_, _nasality_, _sustention_, _sibilation_, _graveness_, and _compactness_. We obtained six recordings for each word,
resulting in 1146 recordings (1152 test items). Only word-initial consonant contrast is tested in the Chinese DRT.

### Chinese (Mandarin) Tonal Contrast
As tone is phonemic in Chinese, a separate word list has been published with minimal pairs testing for tonal contrasts [[2]](#bibliography). This tonal DRT replaces the typical distinctive features
with distinctive tonal contrast (_1&mdash;high level_, _2&mdash;rising_, _3&mdash;low falling rising_, _4&mdash;falling_). Both simplified Chinese and pinyin transcriptions were used to elicit the correct pronunciation in
the recording sessions. We recommend to also present both to participants at test time. The test list contains 40 word pairs (80 unique words). With six recordings per word,
we provide 480 recordings/test items.

### English
We used the DRT list for English that is proposed in [ITU-T Rec. P.807](https://www.itu.int/rec/T-REC-P.807/en) [[3]](#bibliography), as half of the word pairs have phonemic contrast at the beginning of the words (rhyme),
and the other half has phonemic contrast at the end of the words (diagnostic alliteration test). Other word lists exist (e.g., [[4,5]]), but focus exclusively on word-initial contrast.
This test was designed for phonology of North-American varieties of English. Differences in the vowel systems of North-American and other varieties of English lead to a lack of
rhyming contrast in the word pairs _clash_&ndash;_class_, _Slav_&ndash;_slob_, and _flog_&ndash;_flawed_. Care was taken to ensure that these words were pronounced in a North American accent of English.
The word list contains 96 word pairs (190 unique words; _calf_ and _knock_ appear in two word pairs) across the six distinctive feature categories for English
(_voicing_, _nasality_, _sustention_, _sibilation_, _graveness_, _compactness_). Six recordings of each unique word were obtained, leading to a total of 1140 recordings and 1152 test items.

### French
The French DRT materials were recorded without any modification of the word list [[6]](#bibliography). The word list contains 108 word pairs (190 unique words; 23 words occurred in multiple word pairs),
covering the distinctive features relevant to the French phonology (_voicing_, _nasality_, _sustention_, _vowel-likeness_, _graveness_, _compactness_).
With six recordings of each unique word, the dataset contains 1140 recordings to be tested in 1296 test items. Only word-initial consonant contrast is tested in the French DRT.

### German
The German DRT materials were devised for this project in analogy to the English DRT [[7]](#bibliography). Across 96 word pairs devised of 170 unique words,
the distinctive features _voicing_, _nasality_, _sustention_, _sibilation_, _graveness_, and _compactness_ are covered.
One half of the word pairs has phonemic contrast in the word-initial position. Due to the specific phonological constraints of the German language, the other half of the list
has the contrast in either word-final or intervocalic position. Six recordings were obtained for each unique word. A total of 1026 recordings (1152 test items) is provided in this test set.

### Spanish
The Spanish DRT was originally designed for the phonology of European Castillian Spanish [[8]](#bibliography). In order to open the test to a global Spanish-speaking audience,
we omitted the word pairs in the first set of the sibilation category, as they contain the /s/ vs. /&theta;/ contrast, which only exists in European Spanish.
The word list contains word pairs testing word-initial and intervocal consonantal contrast. The files cover the distinctive feature categories
_voicing_, _nasality_, _sustention_, _sibilation_, _graveness_, and _compactness_. A total of 53 word pairs (106 unique words) was recorded six times,
producing a test corpus of 636 recordings/test items.

### DRT Word Lists in Other Languages

Additionally, we have encountered the following DRT versions of further languages in the literature.

- Arabic [[9,10]](#bibliography)
- Dutch [[11]](#bibliography)
- Greek [[12]](#bibliography)
- Italian [[13]](#bibliography)
- Japanese [[14,15]](#bibliography)
- Kurdish [[16]](#bibliography)
- Portuguese [[17]](#bibliography)
- Serbian [[18]](#bibliography)
- Slovak [[19]](#bibliography)
- Thai [[20]](#bibliography)
- Turkish [[21]](#bibliography)

No recordings are provided at this point for these languages. We plan to extend our dataset in the future and are currently preparing Arabic and Japanese for the next release.
If you are aware of materials (word lists and/or recordings) in other languages, please contact us to extend this list. Note that the materials have not been
reviewed and are solely referenced here to provide an easy overview of existing previous work to the research community.

## Data Collection Information

The speech recordings were collected from native speakers of the respective language on the crowdsourcing platforms [Upwork](https://www.upwork.com/) and [Amazon Mechanical Turk](https://www.mturk.com/) as well as internally.
Speakers were asked to use their best available microphone. All words from the word list were presented to the speakers one by one on their screen.
If noise was detected in the speech sample, the word was presented a second time. The files were post-validated by native speaker annotators:
Mispronounced, unintelligible, noisy, and low-quality recordings were excluded from further consideration.
The final gender-balanced test set for each language included six instances of each target word (three female, three male),
with different sets of talkers across words.

## Dataset Contents

Each language folder consists of the following: 
- __audio test files__ with the following technical specifications:
    - 16 kHz sample rate
    - 16 bit precision
    - cropped to include 500 ms leading and trailing silence
    - faded in and out over 100 ms, respectively
    - level-normalized to &ndash;26 dB RMS
- __a meta_testfiles.csv__ providing speaker information for each audio sample:
    - speaker ID
    - speaker gender
    - speaker age group
    - speaker country of origin, approximating speaker accent
- __a test_design.csv__ outlining one pseudo-randomized test design and providing the following additional details:
    - filename
    - target (ground truth transcription)
    - alternative (alternative transcription presented to the participant)
    - transcriptions of target and alternative in Latin script, if the language is written in a different script
    - speaker information, described above
    - block ID to group files into pseudorandomized, gender- and feature-balanced blocks (1 block to be presented to one participant)
    - feature (e.g., _voicing_, _sibilation_, etc.)
    - state (_present_ or _absent_)
    - state label (e.g., _voiced_ or _voiceless_)
    - [SAMPA](https://www.phon.ucl.ac.uk/home/sampa/) transcription of vocalic context
    - SAMPA transcription of the target phoneme
    - SAMPA transcription of the alternative phoneme contrasted with the target phoneme
    - location (_initial_, _final_, or _intervocalic_)


## Bibliography

[1]: L. Lechler and K. Wojcicki, “Crowdsourced multilingual
speech intelligibility testing,” forthcoming.

[2]: I. McLoughlin, “Subjective Intelligibility Testing of Chinese
Speech,” IEEE Trans. Audio Speech Lang. Process., vol. 16,
no. 1, pp. 23–33, 2008.

[3] ITU-T Rec. P.807, “Subjective test methodology for assessing
speech intelligibility,” 2016.

[4] W. D. Voiers, M. Cohen, and J. Mickunas, “Evaluation of
Speech Processing Devices. 1. Intelligibility, Quality, Speaker
Recognizability,” Tech. Rep. AD0627320, Sperry
Rand Research Center, Sudbury, MA, 1965.

[5] Acoustical Society of America, “Method for Measuring the
Intelligibility of Speech over Communication Systems,” 2020,
Version Number: ANSI/ASA S3.2-2020.

[6] J. Peckels and M. Rossi, “Le Test de Diagnostique par Paires
Minimales,” Revue d’Acoustique, vol. 27, pp. 245–262, 1973.

[7] L. Lechler, “The German diagnostic rhyme test,” forthcoming.

[8] M. R. de Cárdenas and V. Marrero, Cuaderno de logoaudiometría: Guía de referencia rápida, Universidad Nacional
de Educación a distancia, 1994.

[9] B. Boudraa, M. Boudraa, and B. Guerin, “Arabic Diagnostic
Rhyme Test using minimal pairs,” J. Acoust. Soc. Amer., vol.
123, p. 3324, 2008.

[10] B. Abuali and M. B. Kurdy, “Full Diacritization of the
Arabic Text to Improve Screen Readers for the Visually Impaired,” Advances in Human-Computer Interaction, vol. 2022,
p. 1186678, 2022, Publisher: Hindawi.

[11] H. J. M. Steeneken, Ontwikkeling en toetsing van een
Nederlandstalige diagnostische rijmtest voor het testen van
spraakkommunikatiekanalen, Instituut voor Zintuigfysiologie
RVO-TNO, 1982.

[12] D. Tsoukalas, J. Mourjopoulos, and G. Kokkinakis, “Speech
enhancement based on audible noise suppression,” IEEE
Transactions on Speech and Audio Processing, vol. 5, no. 6,
pp. 497–514, 1997.

[13] P. Bonaventura, A. Paoloni, F. Canavesio, and P. Usai, “Realizzazione di un test diagnostico di intelligibilità per la lingua
italiana,” Tech. Rep., Fondazione Ugo Bordoni, Rome, 1986.

[14] M. Fujimori, K. Kondo, K. Takano, and K. Nakagawa, “On
a Revised Wordpair List for the Japanese Intelligibility Test,”
2006.

[15] K. Kondo, “The Japanese Diagnostic Rhyme Test,” in Subjective Quality Measurement of Speech: Its Evaluation, Estimation and Applications, K. Kondo, Ed., pp. 21–28.
Springer
Berlin Heidelberg, Berlin, Heidelberg, 2012.

[16] W. Barkhoda, B. ZahirAzami, A. Bahrampour, and O. K.
Shahryari, “A comparison between allophone, syllable, and
diphone based TTS systems for Kurdish language,” in 2009
IEEE
International Symposium on Signal Processing and Information Technology (ISSPIT), Ajman, United Arab Emirates,
2009, pp. 557–562, IEEE.

[17] D. Silva, D. Freitas, and M. S Barros, “A DRT Approach for
Subjective Evaluation of Intelligibility in European Portuguese
Synthetic Speech,” WSEAS Transactions on Computers, vol. 2,
no. 2, 2003.

[18] S. Ostrogonac and M. Secujski, “DRT and SUS intelligibility
tests for synthesized speech in the Serbian language,” in 2011
19thTelecommunications Forum (FOR) Proceedings of Papers.
2011, pp. 659–662, IEEE, Place: Belgrade, Serbia.

[19] M. Rusko and M. Trnka, “Word Tests for Speech Understandability Evaluation in Slovak,” Computer Treatment of Slavic
and East European Languages, VEDA,
Bratislava, pp. 186–
192, 2005, Publisher: Citeseer.

[20] C. Onsuwan, C. Tantibundhit, T. Saimai, N. Saimai, S.
Thatphithakkul, P. Chootrakool, K. Kosawat, and N. Thatphithakkul, “Subjective intelligibility testing and perceptual
study of thai initial and final consonants,” in International
Congress of Phonetic Sciences (ICPhS), Hong Kong, 2011.

[21] O. Orman, Y. Bicil, H. Palaz, M. Dogan, and A. Kanak, “Assessing intelligibility of basic vocoders using turkish diagnostic rhyme test,” in Proceedings of the IEEE 12th Signal Processing and Communications Applications Conference, 2004.,
2004, pp. 560–563.
