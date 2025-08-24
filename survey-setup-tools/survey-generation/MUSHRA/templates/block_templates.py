"""
Cisco Systems, Inc. and its affiliates
"""
"""
Survey templates (MUSHRA) (code from the QSF file)
"""

TESTING_QUESTION = {
    "SurveyID": "SV_2i3hz0WtAQ1Wa8e",
    "Element": "SQ",
    "PrimaryAttribute": "QUESTION_ID",
    "SecondaryAttribute": "X / ${e://Field/total_questions_per_block} QUESTION_TEMPLATE",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_questions_per_block}</span><strong>\n</strong></strong>\n</div>\n\n QUESTION_TEMPLATE \n<html>\n<body>\n  <script>\n    function stopAudio(a) {\n      a.pause();\n      a.currentTime = 0;\n    }\n    function stopAllAudios() {\n      var a = document.getElementsByTagName(\'audio\');\n      for (i = 0; i < a.length; i++) {\n        stopAudio(a[i]);\n      }\n    }\n  </script>\n  <audio id="AUDIO_ID_REFERENCE" src="AUDIO_LINK_REFERENCE"></audio>\n  <div>\n    <button onclick="stopAllAudios(); document.getElementById(\'AUDIO_ID_REFERENCE\').play()">Play</button>\n    <button onclick="stopAudio(document.getElementById(\'0\'))">Stop</button>\n  </div>\n</body>\n</html>\n',
        "QuestionJS": "Qualtrics.SurveyEngine.addOnload(function() {\n    /* Place your JavaScript here to run when the page loads */\n    jQuery(\"td\").css(\"border-left\", \"2px solid WhiteSmoke\");\n    this.hidePreviousButton();\n\n     // Get the question ID\n    let questionId = this.questionId;\n\n    // Track audio elements\n    let audioElements = jQuery(\"audio\");\n\tlet audioPlayed = new Array(audioElements.length).fill(false);\n\n\n    // Add event listeners to all audio elements\n    audioElements.each(function(index, audio) {\n\t\t\n        // When an audio starts playing\n        jQuery(audio).on('play', function() {\n\t\t\t\n\t\t\tif (!audioPlayed[index]) {\n\t\t\t\t// Disable stop button of current audio and change its style\n\t\t\t\tjQuery(this).siblings(\"div\").find(\"button:contains('Stop')\").prop('disabled', true).css({\n\t\t\t\t\t\"opacity\": \"0.5\",\n\t\t\t\t\t\"cursor\": \"not-allowed\"\n\t\t\t\t});\n\t\t\t}else{\n\t\t\t\t// Enable stop button of current audio and change its style\n\t\t\t\tjQuery(this).siblings(\"div\").find(\"button:contains('Stop')\").prop('disabled', false).css({\n\t\t\t\t\t\"opacity\": \"1\",\n\t\t\t\t\t\"cursor\": \"auto\"\n\t\t\t\t});\n\t\t\t}\n\t\t\t\n\t        // Disable and style only unplayed audio elements and buttons\n            audioElements.each(function(i, otherAudio) {\n\t\t\t\tif (i !== index) {\n\t\t\t\t\t\n                    if (!audioPlayed[i]) {\n                        // Disable unplayed audio elements and their buttons\n                        jQuery(otherAudio).prop('disabled', true).css(\"opacity\", \"0.5\");\n                        jQuery(otherAudio).siblings(\"div\").find(\"button\").prop('disabled', true).css({\n                            \"opacity\": \"0.5\",\n                            \"cursor\": \"not-allowed\"\n                        });\n\t\t\t\t\t\t\n                    } else {\n                        // Only disable the stop button for played audios\n                        jQuery(otherAudio).siblings(\"div\").find(\"button:contains('Stop')\").prop('disabled', true).css({\n                            \"opacity\": \"0.5\",\n                            \"cursor\": \"not-allowed\"\n                        });\n                    }\n                }\n            });\n\t\t\t\n\t\t\t\n\t\t\t// Remove any message validation message\n\t\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\t\t\t\n\t\t\tif (existingValidationDiv.length > 0) {\n\t\t\t\t// Update the content of the existing validation div\n\t\t\t\texistingValidationDiv.html(\"\");\n\n\t\t\t}\n        });\n\n        // When an audio ends\n        jQuery(audio).on('ended', function() {\n            audioPlayed[index] = true;\n            // Re-enable and remove styles from all audio elements and buttons\n            audioElements.each(function() {\n                jQuery(this).prop('disabled', false).css(\"opacity\", \"1\");\n                jQuery(this).siblings(\"div\").find(\"button\").prop('disabled', false).css({\n                    \"opacity\": \"1\",\n                    \"cursor\": \"pointer\"\n                });\n            });\n\t\t\t\n\n            // Change the background of the associated buttons to green\n            jQuery(audio).siblings(\"div\").find(\"button\").css(\"background-color\", \"#4CAF50\");\n        });\n\t\t\n\t\t\n\t\t// Add event listener for the stop button\n        jQuery(audio).siblings(\"div\").find(\"button:contains('Stop')\").on('click', function() {\n        \t// Stop the current audio\n            audio.pause();\n            audio.currentTime = 0; // Reset to the beginning\n\n            // Re-enable and remove styles from all audio elements and buttons\n            audioElements.each(function() {\n                jQuery(this).prop('disabled', false).css(\"opacity\", \"1\");\n                jQuery(this).siblings(\"div\").find(\"button\").prop('disabled', false).css({\n                    \"opacity\": \"1\",\n                    \"cursor\": \"pointer\"\n                });\n            });\n\t\t\t\n\t\t\t// Remove any message validation message\n\t\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\n\t\t\tif (existingValidationDiv.length > 0) {\n\t\t\t\t// Update the content of the existing validation div\n\t\t\t\texistingValidationDiv.html(\"\");\n\n\t\t\t}\n\t\t\t\n        });\n\t\t\n    });\n\n\t\n\t// Default validation message template\n\tlet validationHtml = `\n        <div id=\"CUSTOM_VALIDATION\" class=\"ValidationError\" role=\"alert\" data-runtime-show=\"runtime.ErrorMsg\" data-runtime-html=\"runtime.ErrorMsg\">\n        </div>\n    `;\n\n\t// Append the new validation div if it doesn't exist\n    jQuery(\"#Questions\").append(validationHtml);\n\t\n\tdefault_message = \"\";\n\n    // Monitor the Next button click event\n    jQuery(\"#NextButton\").click(function(event) {\n\t\t\n\t\taudioRated = []\n\t\taudioElements.each(function(index) {\n\t\t\tlet questionIdFormatted = questionId + \"\\\\~\" + (index + 1) + \"\\\\~true-result\";\n\t\t \tlet inputElement = jQuery(\"#\" + questionIdFormatted);\n\n\t\t\tif (inputElement.length) {\n\t\t\t\tlet inputValue = parseInt(inputElement.val(), 10);\n\t\t\t\taudioRated.push(inputValue);\n\t\t\t}\n        });\n\t\t\n\n\t\t// Check all audio samples were played\n        if (audioPlayed.length !== audioElements.length || audioPlayed.includes(false)) {\n\t\t\t\n            // Provide feedback to the user\n\t\t\tdefault_message += `\\nFeedback: One or more audio samples were <u><strong>not played</strong></u> to the end. Please make sure\n\t\t\tto listen carefully to all samples and rate them according to your impressions. Please try again.`;\n      \n\t\t}\n\t\t// Check all audios are rated\n\t\telse if (audioRated.some(Number.isNaN)) {\n            // Provide feedback to the user\n            default_message += `\\nFeedback: One or more audio samples were <u><strong>not scored</strong></u>. Please make sure\n\t\t\tto listen carefully to all samples and rate them according to your impressions. Please try again.`;\t\t\n\t\t}\n\t\t\n\t\t// Check if the validation div already exists\n\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\t\t\n\t\tif (default_message != \"\"){\n\t\t\t// Prevent moving to the next question\n\t\t\tevent.stopPropagation();\n\t\t\tevent.preventDefault();\n\t\t\tevent.stopImmediatePropagation();\n\n\t\t\texistingValidationDiv.html(default_message);\n\t\t\tdefault_message = \"\";\n\t\t}\n\t\t\n    });\n\t\n\t});\n\n\n\nQualtrics.SurveyEngine.addOnReady(function()\n    {\n        /*Place your JavaScript here to run when the page is fully displayed*/\n\t\t\n\t\t\t//This is the code related to the number of questions:\n\t\n\t\tlet simpleCounter = Number(\"$e{ e://Field/question_counter_rating_job + 1 }\");\n\n\t\tQualtrics.SurveyEngine.setEmbeddedData('question_counter_rating_job', simpleCounter);\n\n\t\tjQuery(\"#current-page\").html(simpleCounter)\n\n\n\t\tjQuery(\"td\").css(\"border-left\",\"2px solid WhiteSmoke\");\n    });\n\nQualtrics.SurveyEngine.addOnUnload(function()\n    {\n        /*Place your JavaScript here to run when the page is unloaded*/\n\n    });\n\n Qualtrics.SurveyEngine.addOnPageSubmit(function () {\n\t \n\n        var qid = this.questionId;\n        var anchor_ind = ANCHOR_INDEX;\n        var ref_ind = REF_INDEX;\n     \t\n\t \t// Obtain current anchor and reference values\n        var anchor = Number(this.getChoiceValue(anchor_ind));\n        var ref =  Number(this.getChoiceValue(ref_ind));\n\t\t\n\t \t// Flag for anchor type\n\t \tvar anchor_type = \"${e://Field/anchor_type}\";\n\t \n\t \tvar ref_min_threshold = Number(\"${e://Field/ref_threshold}\");\n\t \tvar anchor_max_threshold = Number(\"${e://Field/anchor_threshold}\");\n\t    var anchor_min_distance_wrt_ref = Number(\"${e://Field/min_anchor_distance_wrt_reference}\");\n        \n\t \t// Set anchor max threshold relative to the reference \n\t \tvar anchor_relative_max_threshold = ref - anchor_min_distance_wrt_ref;\n\t \t\n\t \n\t \t// Default anchor selection type\n\t \tvar selected_anchor = anchor_relative_max_threshold;\n\t \t\n\t \t// Adjust threshold\n\t \tif (anchor_type === \"max\"){\n\t\t\tselected_anchor = anchor_max_threshold;\n\t\t};\n\t \n\t\t\n        if (anchor < selected_anchor) {\n            var anchor_low = Number(\"$e{ e://Field/valid_anchor_on_block + 1 }\");\n            Qualtrics.SurveyEngine.setEmbeddedData('valid_anchor_on_block',anchor_low);\n        };\n\t\n\n        if (ref > ref_min_threshold) {\n            var hidden_ref_high = Number(\"$e{ e://Field/valid_hidden_reference_on_block + 1 }\");\n            Qualtrics.SurveyEngine.setEmbeddedData('valid_hidden_reference_on_block',hidden_ref_high);\n        };\n    });",
        "DefaultChoices": False,
        "DataExportTag": "FILENAME_WAV",
        "QuestionType": "Slider",
        "Selector": "HSLIDER",
        "DataVisibility": {"Private": False, "Hidden": False},
        "Configuration": {
            "QuestionDescriptionOption": "UseText",
            "CSSliderMin": 0,
            "CSSliderMax": 100,
            "GridLines": 10,
            "SnapToGrid": False,
            "NumDecimals": "0",
            "ShowValue": True,
            "CustomStart": True,
            "SliderStartPositions": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0},
            "NotApplicable": False,
            "MobileFirst": False,
        },
        "QuestionDescription": "X / ${e://Field/total_questions_per_block} QUESTION_TEMPLATE",
        "Choices": {
            "1": {
                "Display": '<html>\n<body>\n  <script>\n    function stopAudio(a) {\n      a.pause();\n      a.currentTime = 0;\n    }\n    function stopAllAudios() {\n      var a = document.getElementsByTagName(\'audio\');\n      for (i = 0; i < a.length; i++) {\n        stopAudio(a[i]);\n      }\n    }\n  </script>\n  <audio id="13994" src="https://bbl-classification-tool.s3.amazonaws.com/qualtrics/2024_08_14_xcodec_aug24_delivery_1236_v2/bd23b26aa9fb96950aed20c3b93babdfef516f45.wav?AWSAccessKeyId=AKIAV6OBJ7ACHLPNVDU2&Signature=Slsv%2FK%2BUXdwDd727URhJA6aBL64%3D&Expires=1755520428"></audio>\n  <div>\n    <button onclick="stopAllAudios(); document.getElementById(\'13994\').play()">Play</button>\n    <button onclick="stopAudio(document.getElementById(\'13994\'))">Stop</button>\n  </div>\n</body>\n</html>\n'
            }
        },
        "ChoiceOrder": [1, 2, 3, 4, 5, 6],
        "Randomization": {"Advanced": None, "TotalRandSubset": "", "Type": "All"},
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 13,
        "NextAnswerId": 6,
        "Labels": {
            "1": {"Display": "Bad"},
            "2": {"Display": "Poor"},
            "3": {"Display": "Fair"},
            "4": {"Display": "Good"},
            "5": {"Display": "Excellent"},
        },
        "QuestionID": "QUESTION_ID",
    },
}


PASSIVE_TRAINING_QUESTION = {
    "SurveyID": "SV_6X02QTAQZixOwaa",
    "Element": "SQ",
    "PrimaryAttribute": "QUESTION_ID",
    "SecondaryAttribute": "X / ${e://Field/total_passive_training_questions}",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_passive_training_questions}</span><strong>\n</strong></strong>\n</div>\n\n<h1>Training Example: Listening Only</h1>\n<br><br>\n\nThe following is a training example.\n<br><br>\nYour task is to pay close attention to overall quality degradations. This includes (but is not limited to) degradations related to unnatural changes in the talker\'s voice - as compared with the provided reference.\n<br><br>\nThis may include artefacts that you may not be familiar with. \n<br><br>\nThe response regions marked in green \n(<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 0.25); border: 1px solid black;"></span>\n<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 0.5); border: 1px solid black;"></span>\n<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 1); border: 1px solid black;"></span>\n<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 1); border: 1px solid black;"></span>\n<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 0.5); border: 1px solid black;"></span>\n<span style="display: inline-block; width: 15px; height: 15px; background-color: rgba(75, 181, 67, 0.25); border: 1px solid black;"></span>) are plausible examples of response regions to consider when scoring.<br><br>\n\nNote that in order to be able to appreciate the quality differences properly you may require <strong> higher quality wired (ideally over-ear) headphones </strong>.\n<br><br>\n\n\nPlease understand that the task is highly subjective in nature, and hence utilize the regions as approximate guidance, and subject to you own impressions.\n<br><br>\n\nListen carefully, these examples will help you to understand how to complete the survey.\n<br>\n\nYou\'ll need to listen to all the audio examples to continue to the next section.<br><br> \n\n<hr>\n\n${e://Field/survey_main_question}\n<br>\n<br>\n\nReference without distortions:\n  \n<html>\n<body>\n  <script>\n    function stopAudio(a) {\n      a.pause();\n      a.currentTime = 0;\n    }\n    function stopAllAudios() {\n      var a = document.getElementsByTagName(\'audio\');\n      for (i = 0; i < a.length; i++) {\n        stopAudio(a[i]);\n      }\n    }\n  </script>\n  <audio id="AUDIO_ID_REFERENCE" src="AUDIO_LINK_REFERENCE"></audio>\n  <div>\n    <button onclick="stopAllAudios(); document.getElementById(\'AUDIO_ID_REFERENCE\').play()">Play</button>\n    <button onclick="stopAudio(document.getElementById(\'0\'))">Stop</button>\n  </div>\n</body>\n</html>\n',
        "QuestionJS": "Qualtrics.SurveyEngine.addOnload(function()\n    {\n        /*Place your JavaScript here to run when the page loads*/\n        jQuery(\"td\").css(\"border-left\",\"2px solid WhiteSmoke\");\n\t\t\n\t\t// Add custom CSS to hide the slider handles\n\t\tvar handleDivs = document.querySelectorAll('div.handle.selected');\n\t\t\n\t\t// Iterate over the NodeList and hide each element\n\t\thandleDivs.forEach(function(div) {\n\t\t\tdiv.style.display = 'none';\n\t\t});\n\t\n\t\n\t\t// Get the question ID\n\t\tlet questionId = this.questionId;\n\t\n\t\t// Check if the current question already has a stored counter value\n\t\tlet questionCounter = sessionStorage.getItem('question_' + questionId);\n\n\t\tif (!questionCounter) {\n\t\t\t// If not, assign the next counter value\n\t\t\tlet currentCounter = Number(\"${e://Field/question_counter_passive_training}\");\n\t\t\tquestionCounter = currentCounter + 1;\n\n\t\t\t// Store the new counter value in session storage\n\t\t\tsessionStorage.setItem('question_' + questionId, questionCounter);\n\n\t\t\t// Update the embedded data to the new counter value\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData('question_counter_passive_training', questionCounter);\n\t\t}\n\n\t\t// Display the counter value for the current question\n\t\tjQuery(\"#current-page\").html(questionCounter);\n\n\t\t\n\t\t// Check if the audio was already played (session Storage):\n\t\tlet question_already_played = sessionStorage.getItem('played_question_' + questionId);\n\n\t\tif (!question_already_played) {\n\t\t\tthis.hideNextButton();\n\t\t}\n\t\n\t\t\n\t\t// create color map for scores ranges.\n\t\tfunction createColorMap(numbers, rgbaString, alphas) {\n\t\t\t// Extract the RGB components from the RGBA string\n\t\t    const rgbaParts = rgbaString.match(/(\\d+),\\s*(\\d+),\\s*(\\d+),\\s*(\\d+(\\.\\d+)?)/);\n\t\t\tconst r = rgbaParts[1];\n\t\t\tconst g = rgbaParts[2];\n\t\t\tconst b = rgbaParts[3];\n\n\t\t\t// Initialize an empty dictionary\n\t\t\tconst colorMap = {};\n\n\t\t\t// Populate the dictionary with RGBA values\n\t\t\tnumbers.forEach((number, index) => {\n\t\t\t\tconst alpha = alphas[index];\n\t\t\t\tcolorMap[number] = \"rgba(\" + r + \", \" + g + \", \" + b + \", \" + alpha + \")\";\n\t\t\t});\n\t\t\t\n\t\t\treturn colorMap;\n\t\t}\n\n\t\n\t\t// Set positive ranges for conditions\n\t\tvar backgroundColorConditionScoreMap = BACKGROUND_CONDITION_SCORE_MAP;\n\t\t\n\t\t// Set alpha (fade) for all conditions\n\t\tvar alphaFadeColorConditionScoreMap = ALPHA_FADE_COLOR_CONDITION_SCORE_MAP;\t\n\t\n\t    // Captions dictionary\n\t\tvar captionsConfig = CAPTIONS_PER_CONDITION_CONFIG;\n\n\t\t// Function to calculate initial values based on the provided ranges\n\t\tfunction calculateInitialValue(range) {\n\t\t\t// Get the minimum value and subtract 1\n\t\t\tvar min = Math.min(...range) - 1;\n\t\t\t// Get the maximum value\n\t\t\tvar max = Math.max(...range);\n\t\t\t// Calculate the midpoint\n\t\t\tvar midpoint = (max - min) / 2;\n\t\t\t// Return the midpoint multiplied by 10 and cast to an integer\n\t\t\treturn Math.floor( (midpoint + min) * 10);\n\t\t}\n\t\n\t\t\t\t\n\t\tvar sliderQuestion = this;\n\t\tvar areaBackgroundColor = \"rgba(75, 181, 67, 1)\";\n\t\n\t    // Reference to the main element (slider question)\n\t    var mainElement = this.getQuestionContainer();\n\t\n\t\t// Get all tr elements with a choiceid attribute within the main element\n\t\tvar trElements = jQuery(mainElement).find('tr[choiceid]');\n\n\t\t// Loop through each tr element\n\t\ttrElements.each(function() {\n\t\t\tvar tr = jQuery(this);\t\n\t\t    var choiceId = tr.attr('choiceid'); // Get the choiceid value        \t\n\t\t\t\n\t\t\tvar tdIndices = backgroundColorConditionScoreMap[choiceId]; // Get the list of td indices from the dictionary\t\t\t\n\t\t\tvar backgroundAlphas =alphaFadeColorConditionScoreMap[choiceId];\n\t\t\t\n\t\t\t// background colors dictionary\n\t\t\tvar backgroundColorsDict = createColorMap(tdIndices, areaBackgroundColor, backgroundAlphas);\n\t\t\t\n\t\t\t// Calculate the initial value based on tdIndices\n\t\t\tif (tdIndices.length > 0) {\n\t\t\t\tvar initialValue = calculateInitialValue(tdIndices);\n\t\t\t\tsliderQuestion.setChoiceValue(choiceId, initialValue);\n\t\t\t}\n\t\t\t\n\t\t\t// Check if the dictionary has entries for the current choiceid\n\t\t\tif (tdIndices) {\n\t\t\t\ttdIndices.forEach(function(index) {\n\t\t\t\t\t// Construct the class name for the td element (G1, G2, ..., G10)\n\t\t\t\t\tvar className = 'G' + index;\n\t\t\t\t\t\n\t\t\t\t\t// Find the td element with the constructed class name\n\t\t\t\t\tvar tdElement = tr.find('td.' + className);\n\t\t\t\t\ttdElement.css('background-color', backgroundColorsDict[index]);\n\t\t\t\t\t\n\t\t\t\t});\n\t\t\t}\n\t\t\t\n\t\t\t// Disable the slider\n\t\t\ttr.find('.trackHolderRel').addClass('disabled');\n\t\t\ttr.find('.track').attr('aria-disabled', 'true').css('pointer-events', 'none');\n\t\t\t\t\t\n\t\t\t// Get the caption for the current choiceId\n\t\t\tvar caption = captionsConfig[choiceId] || \"\";\n\t\t\n\t\t\t// Create the new tr element with jQuery\n\t\t\tvar newTr = jQuery('<tr>').css('text-align', 'center').css('vertical-align', 'middle');\n\t\t\tvar newTd = jQuery('<td>').css('padding-bottom', '25px').appendTo(newTr);\n\t\t\tvar newSpan = jQuery('<span>').text(caption).appendTo(newTd);\n\n\t\t\t// Add the new tr after the current tr\n\t\t\ttr.after(newTr);\n\n\t});\n\n\t\t// Function to check if all audios have been listened to\n\t\tfunction checkAllAudiosPlayed() {\n\t\t\tvar allPlayed = true;\n\t\t\tjQuery('audio').each(function() {\n\t\t\t\tif (!this.played.length || this.played.end(0) < this.duration) {\n\t\t\t\t\tallPlayed = false;\n\t\t\t\t}\n\t\t\t});\n\t\t\treturn allPlayed;\n\t\t}\n\n\t\t// Monitor the audio elements\n\t\tvar audioElements = jQuery('audio');\n\n\t\taudioElements.each(function() {\n\t\t\tvar audioElement = jQuery(this);\n\t\t\tvar audioId = audioElement.attr('id');\n\n\t\t\t// Find the Play button corresponding to this audio element\n\t\t\tvar playButton = jQuery('button[onclick*=\"' + audioId + '\"]');\n\n\t\t\t// Monitor when the audio starts playing\n\t\t\taudioElement.on('play', function() {\n\t\t\t\t// Reset the play button if playback is restarted\n\t\t\t\tplayButton.css({\n\t\t\t\t\t'background-color': '', // Reset the background color\n\t\t\t\t\t'pointer-events': 'auto', // Enable pointer events\n\t\t\t\t\t'opacity': '1' // Reset opacity\n\t\t\t\t});\n\t\t\t});\n\n\t\t\t// Monitor when the audio ends\n\t\t\taudioElement.on('ended', function() {\n\t\t\t\t// Change the color of the Play button and disable it when audio ends\n\t\t\t\tplayButton.css({\n\t\t\t\t\t'background-color': '#4CAF50', // Change to green\n\t\t\t\t\t'opacity': '0.5' // Optional: Make it appear disabled\n\t\t\t\t});\n\n\t\t\t\t// Check if all audios have been played\n\t\t\t\tif (checkAllAudiosPlayed()) {\n\t\t\t\t\tsliderQuestion.showNextButton();\n\t\t\t\t\tsessionStorage.setItem('played_question_' + questionId, true);\n\t\t\t\t}\n\t\t\t});\n\t\t});\n\t});\n\nQualtrics.SurveyEngine.addOnReady(function()\n    {\n        /*Place your JavaScript here to run when the page is fully displayed*/\n\t\tjQuery(\"td\").css(\"border-left\",\"2px solid WhiteSmoke\");\n    });\n\n Qualtrics.SurveyEngine.addOnUnload(function()\n    {\n        /*Place your JavaScript here to run when the page is unloaded*/\n\n    });\n\n Qualtrics.SurveyEngine.addOnPageSubmit(function () {\n\t /*Place your JavaScript here to run when the page is submitted*/\n\n\n\t \n\n});",
        "DefaultChoices": False,
        "QuestionType": "Slider",
        "Selector": "HSLIDER",
        "DataVisibility": {"Private": False, "Hidden": False},
        "Configuration": {
            "QuestionDescriptionOption": "UseText",
            "CSSliderMin": 0,
            "CSSliderMax": 100,
            "GridLines": 10,
            "SnapToGrid": False,
            "NumDecimals": "0",
            "ShowValue": False,
            "CustomStart": False,
            "SliderStartPositions": {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0},
            "NotApplicable": False,
            "MobileFirst": False,
        },
        "QuestionDescription": "X / ${e://Field/total_passive_training_questions}",
        "Choices": {
            "1": {
                "Display": '<script>\n    function stopAudio(a) {\n      a.pause();\n      a.currentTime = 0;\n    }\n    function stopAllAudios() {\n      var a = document.getElementsByTagName(\'audio\');\n      for (i = 0; i < a.length; i++) {\n        stopAudio(a[i]);\n      }\n    }\n  </script>\n<audio id="AUDIO_ID_REFERENCE" src="https://bbl-classification-tool.s3.us-west-2.amazonaws.com/qualtrics/codec_training/morphing-training/JOINT_MBR_EP830_1kbps.wav?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAV6OBJ7ACHLPNVDU2%2F20241031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20241031T161332Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=93f63b39fbfd3e38d949c806b9b1097fd32444f9691a78bb0de849dfe3d7a6a3">&nbsp;</audio>\n\n<div><button onclick="stopAllAudios(); document.getElementById(\'13994\').play()">Play</button><button onclick="stopAudio(document.getElementById(\'13994\'))">Stop</button></div>\n'
            }
        },
        "ChoiceOrder": [1, 2, 3],
        "Randomization": {"Advanced": None, "TotalRandSubset": "", "Type": "None"},
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
        "GradingData": [],
        "Language": [],
        "NextChoiceId": 13,
        "NextAnswerId": 6,
        "Labels": {
            "1": {"Display": "Bad"},
            "2": {"Display": "Poor"},
            "3": {"Display": "Fair"},
            "4": {"Display": "Good"},
            "5": {"Display": "Excellent"},
        },
        "DataExportTag": "Q338",
        "QuestionID": "QUESTION_ID",
    },
}


DYNAMIC_TRAINING_QUESTION = {
    "SurveyID": "SV_eLJHIkWfT9PgX30",
    "Element": "SQ",
    "PrimaryAttribute": "QUESTION_ID",
    "SecondaryAttribute": "${e://Field/survey_main_question} Play Stop",
    "TertiaryAttribute": None,
    "Payload": {
        "ChoiceOrder": [1, 2, 3, 4],
        "Choices": {
            "1": {
                "Display": '<html>\n    <body>\n      <script>\n        function stopAudio(a) {\n          a.pause();\n          a.currentTime = 0;\n        }\n        function stopAllAudios() {\n          var a = document.getElementsByTagName(\'audio\');\n          for (i = 0; i < a.length; i++) {\n            stopAudio(a[i]);\n          }\n        }\n      </script>\n      <audio id="1" src="https://bbl-classification-tool.s3.amazonaws.com/qualtrics/codec_training/d51f87bd9a0364325386df1494acf3f08d68294c.wav?AWSAccessKeyId=AKIAV6OBJ7ACHLPNVDU2&Signature=ZlIM5G3ipWsr7Jgw8Z%2FUVPuEimU%3D&Expires=1738754584"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'1\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'1\'))">Stop</button>\n      </div>\n    </body>\n    </html>'
            }
        },
        "Configuration": {
            "CSSliderMax": 100,
            "CSSliderMin": 0,
            "CustomStart": True,
            "GridLines": 10,
            "MobileFirst": False,
            "NotApplicable": False,
            "NumDecimals": "0",
            "QuestionDescriptionOption": "UseText",
            "ShowValue": True,
            "SliderStartPositions": {"1": 0, "2": 0, "3": 0, "4": 0},
            "SnapToGrid": False,
        },
        "DataExportTag": "FILENAME_WAV",
        "DataVisibility": {"Hidden": False, "Private": False},
        "DefaultChoices": False,
        "GradingData": [],
        "Labels": {
            "1": {"Display": "Bad"},
            "2": {"Display": "Poor"},
            "3": {"Display": "Fair"},
            "4": {"Display": "Good"},
            "5": {"Display": "Excellent"},
        },
        "Language": [],
        "NextAnswerId": 6,
        "NextChoiceId": 13,
        "QuestionDescription": "X / ${e://Field/total_dynamic_training_questions} ${e://Field/survey_main_question} Play Stop",
        "QuestionID": "QUESTION_ID",
        "QuestionJS": 'Qualtrics.SurveyEngine.addOnload(function()\n{\n\t/*Place your JavaScript here to run when the page loads*/\n\t// Get the question ID\n\tlet questionId = this.questionId;\n\n\t// Check if the current question already has a stored counter value\n\tlet questionCounter = sessionStorage.getItem(\'question_\' + questionId);\n\n\tif (!questionCounter) {\n\t\t// If not, assign the next counter value\n\t\tlet currentCounter = Number(\"${e://Field/question_counter_dynamic_training}\");\n\t\tquestionCounter = currentCounter + 1;\n\n\t\t// Store the new counter value in session storage\n\t\tsessionStorage.setItem(\'question_\' + questionId, questionCounter);\n\n\t\t// Update the embedded data to the new counter value\n\t\tQualtrics.SurveyEngine.setEmbeddedData(\'question_counter_dynamic_training\', questionCounter);\n\t}\n\n\t// Display the counter value for the current question\n\tjQuery(\"#current-page\").html(questionCounter);\n\t\n\t\n\t\n\t// Default validation message template\n\tlet validationHtml = `\n        <div id=\"CUSTOM_VALIDATION\" class=\"ValidationError\" role=\"alert\" data-runtime-show=\"runtime.ErrorMsg\" data-runtime-html=\"runtime.ErrorMsg\">\n        </div>\n    `;\n\n\t// Append the new validation div if it does not exist\n    jQuery(\"#Questions\").append(validationHtml);\n\t\n\tdefault_message = \"\";\n\t\n\n \t// Track audio plays using an array\n    let audioPlayed = [];\n    let audioElements = jQuery(\"audio\");\n\n    // Add event listeners to all audio elements\n    audioElements.each(function(index, audio) {\n        audioPlayed[index] = false;\n\t\t\n        // When an audio starts playing\n        jQuery(audio).on(\'play\', function() {\n\t\t\t\n\t\t\tif (!audioPlayed[index]) {\n\t\t\t\t// Disable stop button of current audio and change its style\n\t\t\t\tjQuery(this).siblings(\"div\").find(\"button:contains(\'Stop\')\").prop(\'disabled\', true).css({\n\t\t\t\t\t\"opacity\": \"0.5\",\n\t\t\t\t\t\"cursor\": \"not-allowed\"\n\t\t\t\t});\n\t\t\t}else{\n\t\t\t\t// Enable stop button of current audio and change its style\n\t\t\t\tjQuery(this).siblings(\"div\").find(\"button:contains(\'Stop\')\").prop(\'disabled\', false).css({\n\t\t\t\t\t\"opacity\": \"1\",\n\t\t\t\t\t\"cursor\": \"auto\"\n\t\t\t\t});\n\t\t\t}\n\t\t\t\n\t        // Disable and style only unplayed audio elements and buttons\n            audioElements.each(function(i, otherAudio) {\n\t\t\t\tif (i !== index) {\n\t\t\t\t\t\n                    if (!audioPlayed[i]) {\n                        // Disable unplayed audio elements and their buttons\n                        jQuery(otherAudio).prop(\'disabled\', true).css(\"opacity\", \"0.5\");\n                        jQuery(otherAudio).siblings(\"div\").find(\"button\").prop(\'disabled\', true).css({\n                            \"opacity\": \"0.5\",\n                            \"cursor\": \"not-allowed\"\n                        });\n\t\t\t\t\t\t\n                    } else {\n                        // Only disable the stop button for played audios\n                        jQuery(otherAudio).siblings(\"div\").find(\"button:contains(\'Stop\')\").prop(\'disabled\', true).css({\n                            \"opacity\": \"0.5\",\n                            \"cursor\": \"not-allowed\"\n                        });\n                    }\n                }\n            });\n\t\t\t\n\t\t\t\n\t\t\t// Remove any message validation message\n\t\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\t\t\t\n\t\t\tif (existingValidationDiv.length > 0) {\n\t\t\t\t// Update the content of the existing validation div\n\t\t\t\texistingValidationDiv.html(\"\");\n\n\t\t\t}\n        });\n\n        // When an audio ends\n        jQuery(audio).on(\'ended\', function() {\n            audioPlayed[index] = true;\n            // Re-enable and remove styles from all audio elements and buttons\n            audioElements.each(function() {\n                jQuery(this).prop(\'disabled\', false).css(\"opacity\", \"1\");\n                jQuery(this).siblings(\"div\").find(\"button\").prop(\'disabled\', false).css({\n                    \"opacity\": \"1\",\n                    \"cursor\": \"pointer\"\n                });\n            });\n\t\t\t\n\n            // Change the background of the associated buttons to green\n            jQuery(audio).siblings(\"div\").find(\"button\").css(\"background-color\", \"#4CAF50\");\n        });\n\t\t\n\t\t\n\t\t// Add event listener for the stop button\n        jQuery(audio).siblings(\"div\").find(\"button:contains(\'Stop\')\").on(\'click\', function() {\n        \t// Stop the current audio\n            audio.pause();\n            audio.currentTime = 0; // Reset to the beginning\n\n            // Re-enable and remove styles from all audio elements and buttons\n            audioElements.each(function() {\n                jQuery(this).prop(\'disabled\', false).css(\"opacity\", \"1\");\n                jQuery(this).siblings(\"div\").find(\"button\").prop(\'disabled\', false).css({\n                    \"opacity\": \"1\",\n                    \"cursor\": \"pointer\"\n                });\n            });\n\t\t\t\n\t\t\t// Remove any message validation message\n\t\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\n\t\t\tif (existingValidationDiv.length > 0) {\n\t\t\t\t// Update the content of the existing validation div\n\t\t\t\texistingValidationDiv.html(\"\");\n\n\t\t\t}\n\t\t\t\n        });\n\t\t\n    });\n\n\t\n  // Event on before next\n    jQuery(\"#NextButton\").click(function(event) {\n\t\t\n\t\t\n\t\t// Ensure the ID is correctly escaped for jQuery selection\n\t\tlet question_id_1 = questionId + \"\\\\~1\\\\~true-result\";\n\t\tlet question_id_2 = questionId + \"\\\\~2\\\\~true-result\";\n\t\tlet question_id_3 = questionId + \"\\\\~3\\\\~true-result\";\n\t\tlet question_id_4 = questionId + \"\\\\~4\\\\~true-result\";\n\t\t\n\t\t\n\t\t// Retrieve the value for every input element\n\t\tlet input_value_q_id_1 = parseInt(jQuery(\"#\" + question_id_1).val(), 10);\n\t\tlet input_value_q_id_2 = parseInt(jQuery(\"#\" + question_id_2).val(), 10);\n\t\tlet input_value_q_id_3 = parseInt(jQuery(\"#\" + question_id_3).val(), 10);\n\t\tlet input_value_q_id_4 = parseInt(jQuery(\"#\" + question_id_4).val(), 10);\n\t\t\t\n\t\t if (audioPlayed.includes(false)) {\n            default_message += `\\nFeedback: One or more audio samples were not played. Please make sure to \n\t\t\tlisten carefully to all samples and rate according to your impressions. Please try again.`;\n        }\n// Check for NaN or zero values\n\t\telse if (isNaN(input_value_q_id_1) || input_value_q_id_1 === 0 ||\n\t\t\tisNaN(input_value_q_id_2) || input_value_q_id_2 === 0 ||\n\t\t\tisNaN(input_value_q_id_3) || input_value_q_id_3 === 0 ||\n\t\t\tisNaN(input_value_q_id_4) || input_value_q_id_4 === 0) {\n\n\t\t\tdefault_message = `\\nFeedback: One or more input values are either Empty or Zero. Please try again.`;\n\t\t} else if (input_value_q_id_1 === 100 && input_value_q_id_2 === 100 &&\n\t\t\t\t   input_value_q_id_3 === 100 && input_value_q_id_4 === 100) {\n\n\t\t\tdefault_message = `\\nFeedback:One of the audio samples sounds exactly as the reference audio \n\t\t\tsample and must be rated with the highest score. Others should be scored lower and according to your impressions. Please try again.`;\n\t\t} else if ( !(input_value_q_id_4 > input_value_q_id_1) || \n\t\t\t\t   !(input_value_q_id_4 > input_value_q_id_2) ||\n\t\t\t\t   !(input_value_q_id_4 > input_value_q_id_3))  {\n\n\t\t\tdefault_message = `\\nFeedback: One of the audio samples sounds exactly as the\n\t\t\treference audio sample and must be rated with the highest score. Please try again.`;\n\t\t\t\n\t\t\t\n\t\t} else if (!(input_value_q_id_2 >= input_value_q_id_1)) {\n\n\t\t\tdefault_message = `\\nFeedback: You have incorrectly rated at least one of the examples lower than the example that has lowest quality. Please try again.`;\n\t\t\t\n\t\t} else if (input_value_q_id_3 < input_value_q_id_1 - 20) {\n\n\t\t\tdefault_message = `\\nFeedback: You have incorrectly rated at least one of the examples much lower than the example that has lowest quality. Please try again.`;\n\t\t\t\n\t\t}else {\n\t\t\tdefault_message = \"\";\n\t\t}\n\t\t\n\t\t// Check if the validation div already exists\n\t\tlet existingValidationDiv = jQuery(\"#CUSTOM_VALIDATION\");\n\n\t\tif (existingValidationDiv.length > 0) {\n\t\t\t// Update the content of the existing validation div\n\t\t\texistingValidationDiv.html(default_message);\n\n\t\t}\n\t\t\n\t\t// If errors, prevent continue\n\t\tvar questionTrainingCounter = parseInt(Qualtrics.SurveyEngine.getEmbeddedData(\"question_training_counter\"));\n\t\tvar trainingAttempsLimit = parseInt(Qualtrics.SurveyEngine.getEmbeddedData(\"training_question_attempts_limit\"));\n\t\tvar trainingPassThreshold = parseInt(Qualtrics.SurveyEngine.getEmbeddedData(\"training_pass_threshold\"));\n\t\t\n\t\t\n\t\tif ( (questionTrainingCounter < trainingAttempsLimit) && default_message != \"\") {\t\n\t\t\t// Prevent moving to the next question\n\t\t\tevent.stopPropagation();\n\t\t\tevent.preventDefault();\n\t\t\tevent.stopImmediatePropagation();\n\t\t\t\n\t\t\t// Update general training errors\n    \t\tvar trainingCounter = parseInt(Qualtrics.SurveyEngine.getEmbeddedData(\"training_counter\")) + 1;\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\"training_counter\", trainingCounter);\n\t\t\t\n\t\t\t\n\t\t\t// Update local training erros\n\t\t\tquestionTrainingCounter += 1\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\"question_training_counter\", questionTrainingCounter);\n\t\t\t\n\t\t\tif (trainingCounter >= trainingPassThreshold){\n\t\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\"allow_extra_rating_job\", \"no\");\n\t\t\t}\n\t\t\t\n\t\t\tdefault_message = \"\";\n\t\t}else{\n\t\t\t// If no errors, continue and reset local training counter for next question\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\"question_training_counter\", 0);\n\t\t}\n\t\t\n\n\n    });\n\t\n\t\n\t// Other styling code\n\tjQuery(\"td\").css(\"border-left\", \"2px solid WhiteSmoke\");\n\t\n\t\n\t\n\n});\n\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n});\n\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});',
        "QuestionText": '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_dynamic_training_questions}</span><strong>\n</strong></strong>\n</div>\n\n\n\n${e://Field/survey_main_question}\n\n<html>\n    <body>\n      <script>\n      function stopAudio(a) {\n        a.pause();\n        a.currentTime = 0;\n      }\n      function stopAllAudios() {\n        var a = document.getElementsByTagName(\'audio\');\n        for (i = 0; i < a.length; i++) {\n          stopAudio(a[i]);\n        }\n      }\n      </script>\n      <audio id="AUDIO_ID_REFERENCE" src="AUDIO_LINK_REFERENCE"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'AUDIO_ID_REFERENCE\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'AUDIO_ID_REFERENCE\'))">Stop</button>\n      </div>\n    </body>\n    </html>',
        "QuestionType": "Slider",
        "Randomization": {"Advanced": None, "TotalRandSubset": "", "Type": "All"},
        "Selector": "HSLIDER",
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
    },
}


CHOISE_TEMPLATE = {
    "Display": '<html>\n<body>\n  <script>\n    function stopAudio(a) {\n      a.pause();\n      a.currentTime = 0;\n    }\n    function stopAllAudios() {\n      var a = document.getElementsByTagName(\'audio\');\n      for (i = 0; i < a.length; i++) {\n        stopAudio(a[i]);\n      }\n    }\n  </script>\n  <audio id="AUDIO_ID" src="AUDIO_LINK"></audio>\n  <div>\n    <button onclick="stopAllAudios(); document.getElementById(\'AUDIO_ID\').play()">Play</button>\n    <button onclick="stopAudio(document.getElementById(\'AUDIO_ID\'))">Stop</button>\n  </div>\n</body>\n</html>\n'
}


CHOISE_TRAINING_TEMPLATE = {
    "1": {
        "Display": '<html>\n    <body>\n      <script>\n        function stopAudio(a) {\n          a.pause();\n          a.currentTime = 0;\n        }\n        function stopAllAudios() {\n          var a = document.getElementsByTagName(\'audio\');\n          for (i = 0; i < a.length; i++) {\n            stopAudio(a[i]);\n          }\n        }\n      </script>\n      <audio id="1" src="ANCHOR_LINK"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'1\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'1\'))">Stop</button>\n      </div>\n    </body>\n    </html>'
    },
    "2": {
        "Display": '<html>\n    <body>\n      <script>\n        function stopAudio(a) {\n          a.pause();\n          a.currentTime = 0;\n        }\n        function stopAllAudios() {\n          var a = document.getElementsByTagName(\'audio\');\n          for (i = 0; i < a.length; i++) {\n            stopAudio(a[i]);\n          }\n        }\n      </script>\n      <audio id="2" src="CONDITION_1_LINK"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'2\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'2\'))">Stop</button>\n      </div>\n    </body>\n    </html>'
    },
    "3": {
        "Display": '<html>\n    <body>\n      <script>\n        function stopAudio(a) {\n          a.pause();\n          a.currentTime = 0;\n        }\n        function stopAllAudios() {\n          var a = document.getElementsByTagName(\'audio\');\n          for (i = 0; i < a.length; i++) {\n            stopAudio(a[i]);\n          }\n        }\n      </script>\n      <audio id="3" src="CONDITION_2_LINK"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'3\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'3\'))">Stop</button>\n      </div>\n    </body>\n    </html>'
    },
    "4": {
        "Display": '<html>\n    <body>\n      <script>\n        function stopAudio(a) {\n          a.pause();\n          a.currentTime = 0;\n        }\n        function stopAllAudios() {\n          var a = document.getElementsByTagName(\'audio\');\n          for (i = 0; i < a.length; i++) {\n            stopAudio(a[i]);\n          }\n        }\n      </script>\n      <audio id="4" src="REFERENCE_LINK"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'4\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'4\'))">Stop</button>\n      </div>\n    </body>\n    </html>'
    },
}


TRAINING_REFERENCE_QUESTION_TEMPLATE = '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_dynamic_training_questions}</span><strong>\n</strong></strong>\n</div>\n\n\n\n Imagine that you are taking part in an extended (one-hour long) conference call. Rate the quality of each audio sample compared to the reference: <br/><br/> Reference:\n    <html>\n    <body>\n      <script>\n      function stopAudio(a) {\n        a.pause();\n        a.currentTime = 0;\n      }\n      function stopAllAudios() {\n        var a = document.getElementsByTagName(\'audio\');\n        for (i = 0; i < a.length; i++) {\n          stopAudio(a[i]);\n        }\n      }\n      </script>\n      <audio id="0" src="REFERENCE_LINK"></audio>\n      <div>\n        <button onclick="stopAllAudios(); document.getElementById(\'0\').play()">Play</button>\n        <button onclick="stopAudio(document.getElementById(\'0\'))">Stop</button>\n      </div>\n    </body>\n    </html>'


BLOCK_TEMPLATE = {
    "Type": "Standard",
    "SubType": "",
    "Description": "DESCRIPTION_ID_PLACEHOLDER",
    "ID": "BLOCK_ID_PLACEHOLDER",
    "BlockElements": [
        {"Type": "Question", "QuestionID": "QID24"},
        {"Type": "Page Break"},
    ],
    "Options": {
        "BlockLocking": "False",
        "RandomizeQuestions": "Advanced",
        "BlockVisibility": "Expanded",
        "Randomization": {
            "Advanced": {
                "FixedOrder": [
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                    "{~Randomized~}",
                ],
                "RandomizeAll": [
                    "QID42",
                    "QID43",
                    "QID44",
                    "QID45",
                    "QID46",
                    "QID47",
                    "QID48",
                    "QID49",
                    "QID50",
                    "QID51",
                ],
                "RandomSubSet": [],
                "Undisplayed": [],
                "TotalRandSubset": 0,
                "QuestionsPerPage": "1",
            },
            "EvenPresentation": False,
        },
    },
}

# Template for the randomizer block (testing)
FLOW_BLOCK_TEMPLATE = {
    "Type": "BlockRandomizer",
    "FlowID": "FL_28",
    "SubSet": 3,
    "EvenPresentation": True,
    "Flow": [],
}


FLOW_BLOCK_RANDOMIZER_ITEM = {
    "Type": "Branch",
    "FlowID": "GENERAL_FLOW_ID",
    "Description": "New Branch",
    "BranchLogic": {
        "0": {
            "0": {
                "LogicType": "EmbeddedField",
                "LeftOperand": "BLOCK_N_SELECTED",
                "Operator": "EqualTo",
                "RightOperand": "0",
                "_HiddenExpression": False,
                "Type": "Expression",
                "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">BLOCK_N_SELECTED</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 0 </span>',
            },
            "Type": "If",
        },
        "Type": "BooleanExpression",
    },
    "Flow": [
        {
            "Type": "EmbeddedData",
            "FlowID": "FL_14",
            "EmbeddedData": [
                {
                    "Description": "anchor_low",
                    "Type": "Custom",
                    "Field": "anchor_low",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "0",
                },
                {
                    "Description": "hidden_ref_high",
                    "Type": "Custom",
                    "Field": "hidden_ref_high",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "0",
                },
            ],
        },
        {
            "Type": "Standard",
            "ID": "BL_0fc2ttLXoVjKe7s",
            "FlowID": "FL_15",
            "Autofill": [],
        },
        {"Type": "Standard", "ID": "BLOCK_ID", "FlowID": "FL_16", "Autofill": []},
        {
            "Type": "EmbeddedData",
            "FlowID": "FL_17",
            "EmbeddedData": [
                {
                    "Description": "anchor_low",
                    "Type": "Custom",
                    "Field": "anchor_low",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "$e{ e://Field/valid_anchor_on_block }",
                },
                {
                    "Description": "hidden_ref_high",
                    "Type": "Custom",
                    "Field": "hidden_ref_high",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "$e{ e://Field/valid_hidden_reference_on_block }",
                },
                {
                    "Description": "number_of_rating_jobs_taken",
                    "Type": "Custom",
                    "Field": "number_of_rating_jobs_taken",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "$e{ e://Field/number_of_rating_jobs_taken + 1 }",
                },
                {
                    "Description": "BLOCK_N_SELECTED",
                    "Type": "Custom",
                    "Field": "BLOCK_N_SELECTED",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "1",
                },
                {
                    "Description": "question_counter_rating_job",
                    "Type": "Custom",
                    "Field": "question_counter_rating_job",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "0",
                },
                {
                    "Description": "valid_anchor_on_block",
                    "Type": "Custom",
                    "Field": "valid_anchor_on_block",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "0",
                },
                {
                    "Description": "valid_hidden_reference_on_block",
                    "Type": "Custom",
                    "Field": "valid_hidden_reference_on_block",
                    "VariableType": "String",
                    "DataVisibility": [],
                    "AnalyzeText": False,
                    "Value": "0",
                },
            ],
        },
        {
            "Type": "Branch",
            "FlowID": "FL_18",
            "Description": "New Branch",
            "BranchLogic": {
                "0": {
                    "0": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "number_of_rating_jobs_taken",
                        "Operator": "EqualTo",
                        "RightOperand": "3",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 3 </span>',
                    },
                    "Type": "If",
                },
                "Type": "BooleanExpression",
            },
            "Flow": [
                {
                    "Type": "EmbeddedData",
                    "FlowID": "FL_35",
                    "EmbeddedData": [
                        {
                            "Description": "bonus",
                            "Type": "Custom",
                            "Field": "bonus",
                            "VariableType": "String",
                            "DataVisibility": [],
                            "AnalyzeText": False,
                            "Value": "${e://Field/bonus_3_blocks}",
                        },
                        {
                            "Description": "approve",
                            "Type": "Custom",
                            "Field": "approve",
                            "VariableType": "String",
                            "DataVisibility": [],
                            "AnalyzeText": False,
                            "Value": "1",
                        },
                        {
                            "Description": "reviewer_feedback",
                            "Type": "Custom",
                            "Field": "reviewer_feedback",
                            "VariableType": "String",
                            "DataVisibility": [],
                            "AnalyzeText": False,
                            "Value": "You have passed all our attention checks. In addition to the task reward ($ ${e://Field/base_pay}), you have earned a bonus of $ ${e://Field/bonus_3_blocks}.",
                        },
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_88",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "deployment_platform",
                                "Operator": "EqualTo",
                                "RightOperand": "dev",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_89",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "SurveyTermination": "DisplayMessage",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "EOSMessage": "MS_3CeRFoRymXPPNtC",
                            },
                        }
                    ],
                },
                {
                    "Type": "EndSurvey",
                    "FlowID": "FL_36",
                    "EndingType": "Advanced",
                    "Options": {
                        "Advanced": "true",
                        "EOSMessage": "MS_WKfkF2W5wknav29",
                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                        "SurveyTermination": "DisplayMessage",
                    },
                },
            ],
        },
        {
            "Type": "Branch",
            "FlowID": "FL_19",
            "Description": "New Branch",
            "BranchLogic": {
                "0": {
                    "0": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "anchor_low",
                        "Operator": "GreaterThanOrEqual",
                        "RightOperand": "${e://Field/anchor_correct_answers_threshold}",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">anchor_low</span> <span class="OpDesc">Is Greater Than or Equal to</span> <span class="RightOpDesc"> ${e://Field/anchor_correct_answers_threshold} </span>',
                    },
                    "1": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "hidden_ref_high",
                        "Operator": "GreaterThanOrEqual",
                        "RightOperand": "${e://Field/ref_correct_answers_threshold}",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">hidden_ref_high</span> <span class="OpDesc">Is Greater Than or Equal to</span> <span class="RightOpDesc"> ${e://Field/ref_correct_answers_threshold} </span>',
                        "Conjuction": "And",
                    },
                    "2": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "allow_extra_rating_job",
                        "Operator": "EqualTo",
                        "RightOperand": "yes",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">allow_extra_rating_job</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> yes </span>',
                        "Conjuction": "And",
                    },
                    "Type": "If",
                },
                "Type": "BooleanExpression",
            },
            "Flow": [
                {
                    "Type": "EmbeddedData",
                    "FlowID": "FL_23",
                    "EmbeddedData": [
                        {
                            "Description": "post_validated",
                            "Type": "Custom",
                            "Field": "post_validated",
                            "VariableType": "String",
                            "DataVisibility": [],
                            "AnalyzeText": False,
                            "Value": "1",
                        }
                    ],
                },
                {
                    "Type": "Standard",
                    "ID": "BL_3JjMrCuRSvIXxDE",
                    "FlowID": "FL_24",
                    "Autofill": [],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_25",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "Question",
                                "QuestionID": "QID23",
                                "QuestionIsInLoop": "no",
                                "ChoiceLocator": "q://QID23/SelectableChoice/1",
                                "Operator": "Selected",
                                "QuestionIDFromLocator": "QID23",
                                "LeftOperand": "q://QID23/SelectableChoice/1",
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="QuestionDesc">You have completed the rating job successfully. If you wish, you may take another rating job for...</span> <span class="LeftOpDesc">Take one more rating job</span> <span class="OpDesc">Is Selected</span> ',
                            },
                            "1": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "1",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 1 </span>',
                                "Conjuction": "And",
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_34",
                            "EmbeddedData": [
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_1_blocks}",
                                },
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                            ],
                        }
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_26",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "Question",
                                "QuestionID": "QID23",
                                "QuestionIsInLoop": "no",
                                "ChoiceLocator": "q://QID23/SelectableChoice/1",
                                "Operator": "Selected",
                                "QuestionIDFromLocator": "QID23",
                                "LeftOperand": "q://QID23/SelectableChoice/1",
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="QuestionDesc">You have completed the rating job successfully. If you wish, you may take another rating job for...</span> <span class="LeftOpDesc">Take one more rating job</span> <span class="OpDesc">Is Selected</span> ',
                            },
                            "1": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "2",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 2 </span>',
                                "Conjuction": "And",
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_33",
                            "EmbeddedData": [
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_2_blocks}",
                                },
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                            ],
                        }
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_27",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "Question",
                                "QuestionID": "QID23",
                                "QuestionIsInLoop": "no",
                                "ChoiceLocator": "q://QID23/SelectableChoice/2",
                                "Operator": "Selected",
                                "QuestionIDFromLocator": "QID23",
                                "LeftOperand": "q://QID23/SelectableChoice/2",
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="QuestionDesc">You have completed the rating job successfully. If you wish, you may take another rating job for...</span> <span class="LeftOpDesc">Proceed to the submission page</span> <span class="OpDesc">Is Selected</span> ',
                            },
                            "1": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "1",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 1 </span>',
                                "Conjuction": "And",
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_31",
                            "EmbeddedData": [
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_1_blocks}",
                                },
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                                {
                                    "Description": "reviewer_feedback",
                                    "Type": "Custom",
                                    "Field": "reviewer_feedback",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "You have passed all requirements for this task. In addition to the task reward ($ ${e://Field/base_pay}), you have earned a bonus of $ ${e://Field/bonus_1_blocks}.",
                                },
                            ],
                        },
                        {
                            "Type": "Branch",
                            "FlowID": "FL_90",
                            "Description": "New Branch",
                            "BranchLogic": {
                                "0": {
                                    "0": {
                                        "LogicType": "EmbeddedField",
                                        "LeftOperand": "deployment_platform",
                                        "Operator": "EqualTo",
                                        "RightOperand": "dev",
                                        "_HiddenExpression": False,
                                        "Type": "Expression",
                                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                                    },
                                    "Type": "If",
                                },
                                "Type": "BooleanExpression",
                            },
                            "Flow": [
                                {
                                    "Type": "EndSurvey",
                                    "FlowID": "FL_91",
                                    "EndingType": "Advanced",
                                    "Options": {
                                        "Advanced": "true",
                                        "SurveyTermination": "DisplayMessage",
                                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                        "EOSMessage": "MS_3CeRFoRymXPPNtC",
                                    },
                                }
                            ],
                        },
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_32",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "EOSMessage": "MS_WKfkF2W5wknav29",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "SurveyTermination": "DisplayMessage",
                            },
                        },
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_28",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "Question",
                                "QuestionID": "QID23",
                                "QuestionIsInLoop": "no",
                                "ChoiceLocator": "q://QID23/SelectableChoice/2",
                                "Operator": "Selected",
                                "QuestionIDFromLocator": "QID23",
                                "LeftOperand": "q://QID23/SelectableChoice/2",
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="QuestionDesc">You have completed the rating job successfully. If you wish, you may take another rating job for...</span> <span class="LeftOpDesc">Proceed to the submission page</span> <span class="OpDesc">Is Selected</span> ',
                            },
                            "1": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "2",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">And</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 2 </span>',
                                "Conjuction": "And",
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_29",
                            "EmbeddedData": [
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_2_blocks}",
                                },
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                                {
                                    "Description": "reviewer_feedback",
                                    "Type": "Custom",
                                    "Field": "reviewer_feedback",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "You have passed all requirements for this task. In addition to the task reward ($ ${e://Field/base_pay}), you have earned a bonus of $ ${e://Field/bonus_2_blocks}.",
                                },
                            ],
                        },
                        {
                            "Type": "Branch",
                            "FlowID": "FL_93",
                            "Description": "New Branch",
                            "BranchLogic": {
                                "0": {
                                    "0": {
                                        "LogicType": "EmbeddedField",
                                        "LeftOperand": "deployment_platform",
                                        "Operator": "EqualTo",
                                        "RightOperand": "dev",
                                        "_HiddenExpression": False,
                                        "Type": "Expression",
                                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                                    },
                                    "Type": "If",
                                },
                                "Type": "BooleanExpression",
                            },
                            "Flow": [
                                {
                                    "Type": "EndSurvey",
                                    "FlowID": "FL_94",
                                    "EndingType": "Advanced",
                                    "Options": {
                                        "Advanced": "true",
                                        "SurveyTermination": "DisplayMessage",
                                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                        "EOSMessage": "MS_3CeRFoRymXPPNtC",
                                    },
                                }
                            ],
                        },
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_30",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "EOSMessage": "MS_WKfkF2W5wknav29",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "SurveyTermination": "DisplayMessage",
                            },
                        },
                    ],
                },
            ],
        },
        {
            "Type": "Branch",
            "FlowID": "FL_20",
            "Description": "New Branch",
            "BranchLogic": {
                "0": {
                    "0": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "anchor_low",
                        "Operator": "LessThan",
                        "RightOperand": "${e://Field/anchor_correct_answers_threshold}",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">anchor_low</span> <span class="OpDesc">Is Less Than</span> <span class="RightOpDesc"> ${e://Field/anchor_correct_answers_threshold} </span>',
                    },
                    "1": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "hidden_ref_high",
                        "Operator": "LessThan",
                        "RightOperand": "${e://Field/ref_correct_answers_threshold}",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">Or</span> <span class="LeftOpDesc">hidden_ref_high</span> <span class="OpDesc">Is Less Than</span> <span class="RightOpDesc"> ${e://Field/ref_correct_answers_threshold} </span>',
                        "Conjuction": "Or",
                    },
                    "2": {
                        "LogicType": "EmbeddedField",
                        "LeftOperand": "allow_extra_rating_job",
                        "Operator": "EqualTo",
                        "RightOperand": "no",
                        "_HiddenExpression": False,
                        "Type": "Expression",
                        "Description": '<span class="ConjDesc">Or</span> <span class="LeftOpDesc">allow_extra_rating_job</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> no </span>',
                        "Conjuction": "Or",
                    },
                    "Type": "If",
                },
                "Type": "BooleanExpression",
            },
            "Flow": [
                {
                    "Type": "Branch",
                    "FlowID": "FL_110",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "1",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 1 </span>',
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_21",
                            "EmbeddedData": [
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_1_blocks}",
                                },
                                {
                                    "Description": "reviewer_feedback",
                                    "Type": "Custom",
                                    "Field": "reviewer_feedback",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "You did not achieve the minimum number of correct answers in the attention checks. You will receive the compensantion for the task you completed: $ $e{ ${e://Field/base_pay} + ${e://Field/bonus} }.",
                                },
                            ],
                        },
                        {
                            "Type": "Branch",
                            "FlowID": "FL_95",
                            "Description": "New Branch",
                            "BranchLogic": {
                                "0": {
                                    "0": {
                                        "LogicType": "EmbeddedField",
                                        "LeftOperand": "deployment_platform",
                                        "Operator": "EqualTo",
                                        "RightOperand": "dev",
                                        "_HiddenExpression": False,
                                        "Type": "Expression",
                                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                                    },
                                    "Type": "If",
                                },
                                "Type": "BooleanExpression",
                            },
                            "Flow": [
                                {
                                    "Type": "EndSurvey",
                                    "FlowID": "FL_96",
                                    "EndingType": "Advanced",
                                    "Options": {
                                        "Advanced": "true",
                                        "SurveyTermination": "DisplayMessage",
                                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                        "EOSMessage": "MS_3CeRFoRymXPPNtC",
                                    },
                                }
                            ],
                        },
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_22",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "EOSMessage": "MS_WKfkF2W5wknav29",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "SurveyTermination": "DisplayMessage",
                            },
                        },
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_111",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "2",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 2 </span>',
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_112",
                            "EmbeddedData": [
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_2_blocks}",
                                },
                                {
                                    "Description": "reviewer_feedback",
                                    "Type": "Custom",
                                    "Field": "reviewer_feedback",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "You did not achieve the minimum number of correct answers in the attention checks. You will receive the compensantion for the 2 tasks you completed: $ $e{ ${e://Field/base_pay} + ${e://Field/bonus} }.",
                                },
                            ],
                        },
                        {
                            "Type": "Branch",
                            "FlowID": "FL_113",
                            "Description": "New Branch",
                            "BranchLogic": {
                                "0": {
                                    "0": {
                                        "LogicType": "EmbeddedField",
                                        "LeftOperand": "deployment_platform",
                                        "Operator": "EqualTo",
                                        "RightOperand": "dev",
                                        "_HiddenExpression": False,
                                        "Type": "Expression",
                                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                                    },
                                    "Type": "If",
                                },
                                "Type": "BooleanExpression",
                            },
                            "Flow": [
                                {
                                    "Type": "EndSurvey",
                                    "FlowID": "FL_114",
                                    "EndingType": "Advanced",
                                    "Options": {
                                        "Advanced": "true",
                                        "SurveyTermination": "DisplayMessage",
                                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                        "EOSMessage": "MS_3CeRFoRymXPPNtC",
                                    },
                                }
                            ],
                        },
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_115",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "EOSMessage": "MS_WKfkF2W5wknav29",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "SurveyTermination": "DisplayMessage",
                            },
                        },
                    ],
                },
                {
                    "Type": "Branch",
                    "FlowID": "FL_119",
                    "Description": "New Branch",
                    "BranchLogic": {
                        "0": {
                            "0": {
                                "LogicType": "EmbeddedField",
                                "LeftOperand": "number_of_rating_jobs_taken",
                                "Operator": "EqualTo",
                                "RightOperand": "3",
                                "_HiddenExpression": False,
                                "Type": "Expression",
                                "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">number_of_rating_jobs_taken</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> 3 </span>',
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Flow": [
                        {
                            "Type": "EmbeddedData",
                            "FlowID": "FL_120",
                            "EmbeddedData": [
                                {
                                    "Description": "approve",
                                    "Type": "Custom",
                                    "Field": "approve",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "1",
                                },
                                {
                                    "Description": "bonus",
                                    "Type": "Custom",
                                    "Field": "bonus",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "${e://Field/bonus_3_blocks}",
                                },
                                {
                                    "Description": "reviewer_feedback",
                                    "Type": "Custom",
                                    "Field": "reviewer_feedback",
                                    "VariableType": "String",
                                    "DataVisibility": [],
                                    "AnalyzeText": False,
                                    "Value": "You did not achieve the minimum number of correct answers in the attention checks. You will receive the compensantion for the 3 tasks you completed: $ $e{ ${e://Field/base_pay} + ${e://Field/bonus} }.",
                                },
                            ],
                        },
                        {
                            "Type": "Branch",
                            "FlowID": "FL_121",
                            "Description": "New Branch",
                            "BranchLogic": {
                                "0": {
                                    "0": {
                                        "LogicType": "EmbeddedField",
                                        "LeftOperand": "deployment_platform",
                                        "Operator": "EqualTo",
                                        "RightOperand": "dev",
                                        "_HiddenExpression": False,
                                        "Type": "Expression",
                                        "Description": '<span class="ConjDesc">If</span> <span class="LeftOpDesc">deployment_platform</span> <span class="OpDesc">Is Equal to</span> <span class="RightOpDesc"> dev </span>',
                                    },
                                    "Type": "If",
                                },
                                "Type": "BooleanExpression",
                            },
                            "Flow": [
                                {
                                    "Type": "EndSurvey",
                                    "FlowID": "FL_122",
                                    "EndingType": "Advanced",
                                    "Options": {
                                        "Advanced": "true",
                                        "SurveyTermination": "DisplayMessage",
                                        "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                        "EOSMessage": "MS_3CeRFoRymXPPNtC",
                                    },
                                }
                            ],
                        },
                        {
                            "Type": "EndSurvey",
                            "FlowID": "FL_123",
                            "EndingType": "Advanced",
                            "Options": {
                                "Advanced": "true",
                                "EOSMessage": "MS_WKfkF2W5wknav29",
                                "EOSMessageLibrary": "GR_bl8pfgbNaQKY2DY",
                                "SurveyTermination": "DisplayMessage",
                            },
                        },
                    ],
                },
            ],
        },
    ],
}


DYNAMIC_TRAINING_BLOCK_TEMPLATE = {
    "BlockElements": [{"QuestionID": "QID59", "Type": "Question"}],
    "Description": "DESCRIPTION_ID_PLACEHOLDER",
    "ID": "BLOCK_ID_PLACEHOLDER",
    "Options": {
        "BlockLocking": "false",
        "BlockVisibility": "Collapsed",
        "Looping": "None",
        "LoopingOptions": None,
        "RandomizeQuestions": "false",
    },
    "SubType": "",
    "Type": "Standard",
}

# Template for the randomizer block (dynamic training)
FLOW_DYNAMIC_TRAINING_BLOCK_TEMPLATE = {
    "Type": "BlockRandomizer",
    "FlowID": "FL_47",
    "SubSet": 3,
    "Flow": [],
}


FLOW_BLOCK_DYNAMIC_TRAINING_RANDOMIZER_ITEM = {
    "Type": "Standard",
    "ID": "BLOCK_ID",
    "FlowID": "GENERAL_FLOW_ID",
    "Autofill": [],
}


HEARING_TEST_TEMPLATE = {
    "SurveyID": "SV_03C5SeSRkqDaFme",
    "Element": "SQ",
    "PrimaryAttribute": "QID54",
    "SecondaryAttribute": "\u00a0 Hearing Test \u00a0 Please note that this is not a medical test but a quick method for us to check y.",
    "TertiaryAttribute": None,
    "Payload": {
        "AnswerOrder": ["1", "2", "3", "4", "5", "6"],
        "AnswerRandomization": {
            "Advanced": None,
            "TotalRandSubset": "",
            "Type": "None",
        },
        "Answers": {
            "1": {
                "Display": '<button id="audiobutton1" type="button">Play</button>\n<audio id="audiofile1" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
            "2": {
                "Display": '<button id="audiobutton2" type="button">Play</button>\n<audio id="audiofile2" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
            "3": {
                "Display": '<button id="audiobutton3" type="button">Play</button>\n<audio id="audiofile3" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
            "4": {
                "Display": '<button id="audiobutton4" type="button">Play</button>\n<audio id="audiofile4" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
            "5": {
                "Display": '<button id="audiobutton5" type="button">Play</button>\n<audio id="audiofile5" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
            "6": {
                "Display": '<button id="audiobutton6" type="button">Play</button>\n<audio id="audiofile6" src="AUDIO_LINK_PLACEHOLDER">&nbsp;</audio>\n'
            },
        },
        "ChoiceDataExportTags": False,
        "ChoiceOrder": ["4"],
        "Choices": {"4": {"Display": "Digits:"}},
        "Configuration": {
            "ChoiceColumnWidth": 25,
            "MobileFirst": True,
            "QuestionDescriptionOption": "UseText",
            "RepeatHeaders": "none",
            "TextPosition": "inline",
        },
        "DataExportTag": "Q10",
        "DataVisibility": {"Hidden": False, "Private": False},
        "DefaultChoices": False,
        "GradingData": [],
        "Language": [],
        "NextAnswerId": 7,
        "NextChoiceId": 5,
        "QuestionDescription": "\u00a0 Hearing Test \u00a0 Please note that this is not a medical test but a quick method for us to check y...",
        "QuestionID": "QID54",
        "QuestionJS": 'Qualtrics.SurveyEngine.addOnload(function()\n{\n\tthis.hidePreviousButton();\n\t//create variable to track play count\n\tvar playcount1 = 0; \n\tvar playcount2 = 0; \n\tvar playcount3 = 0; \n\tvar playcount4 = 0; \n\tvar playcount5 = 0; \n\tvar playcount6 = 0; \n\t//create variable to track page refresh count \n\tvar refreshcount = 0;\n\t//Get audio element\n\t//name "audiofile1" this whatever you name your audio element ID is within your HTML \n\tvar audio1 = document.getElementById("audiofile1"); \n\tvar audio2 = document.getElementById("audiofile2"); \n\tvar audio3 = document.getElementById("audiofile3"); \n\tvar audio4 = document.getElementById("audiofile4"); \n\tvar audio5 = document.getElementById("audiofile5"); \n\tvar audio6 = document.getElementById("audiofile6"); \n\taudio1.volume = 1; //set audio volume to 1\n\taudio2.volume = 1; //set audio volume to 1\n\taudio3.volume = 1; //set audio volume to 1\n\taudio4.volume = 1; //set audio volume to 1\n\taudio5.volume = 1; //set audio volume to 1\n\taudio6.volume = 1; //set audio volume to 1\n\tvar button1 = document.getElementById("audiobutton1"); //grab button id\n\tvar button2 = document.getElementById("audiobutton2"); //grab button id\n\tvar button3 = document.getElementById("audiobutton3"); //grab button id\n\tvar button4 = document.getElementById("audiobutton4"); //grab button id\n\tvar button5 = document.getElementById("audiobutton5"); //grab button id\n\tvar button6 = document.getElementById("audiobutton6"); //grab button id\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count1", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count2", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count3", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count4", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count5", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData("play_count6", 0);\n\t\n// CREATE playAudio() FUNCTION\nfunction playAudio1() {\n  playcount1++; //increase playcount number by 1\n  console.log(playcount1); \n  audio1.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count1", playcount1); \n};\n\nfunction playAudio2() {\n  playcount2++; //increase playcount number by 1\n  console.log(playcount2); \n  audio2.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count2", playcount2); \n};\n\nfunction playAudio3() {\n  playcount3++; //increase playcount number by 1\n  console.log(playcount3); \n  audio3.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count3", playcount3); \n};\n\t\nfunction playAudio4() {\n  playcount4++; //increase playcount number by 1\n  console.log(playcount4); \n  audio4.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count4", playcount4); \n};\n\nfunction playAudio5() {\n  playcount5++; //increase playcount number by 1\n  console.log(playcount5); \n  audio5.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count5", playcount5); \n};\n\t\nfunction playAudio6() {\n  playcount6++; //increase playcount number by 1\n  console.log(playcount6); \n  audio6.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData("play_count6", playcount6); \n};\n\t\naudio1.onended = function() {\n\tif (playcount1 < 5){\n\t\tbutton1.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton1.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\t\naudio2.onended = function() {\n\tif (playcount2 < 5){\n\t\tbutton2.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton2.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\t\naudio3.onended = function() {\n\tif (playcount3 < 5){\n\t\tbutton3.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton3.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\t\naudio4.onended = function() {\n\tif (playcount4 < 5){\n\t\tbutton4.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton4.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\t\naudio5.onended = function() {\n\tif (playcount5 < 5){\n\t\tbutton5.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton5.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\naudio6.onended = function() {\n\tif (playcount6 < 5){\n\t\tbutton6.style.visibility = "visible"; //show button again\n\t} else {\n\t\tbutton6.style.visibility = "hidden"; //hide the button so that it can\'t be played anymore\n\t}\n}; \n\n// TRIGGER playAudio() function on button press (note that the HTML element id for the button is called "audiobutton"\njQuery("#audiobutton1").on("click", playAudio1);\njQuery("#audiobutton2").on("click", playAudio2);\njQuery("#audiobutton3").on("click", playAudio3);\njQuery("#audiobutton4").on("click", playAudio4);\njQuery("#audiobutton5").on("click", playAudio5);\njQuery("#audiobutton6").on("click", playAudio6);\n\n\n// TRACKING PAGE REFRESH\n// NOTE: "playcount" variable refreshs to 0 if a respondent refreshes the page\n\t// WARNING: The three lines below will not work properly if this JavaScript is on the first page of the survey\n\t\n// Pull number in pageload (default within embedded data element should be set to 0)\nvar pageload = Qualtrics.SurveyEngine.getEmbeddedData(\'pageload_count\');\npageload = parseInt(pageload)+1; \n//save updated reload value to \'refresh_count\' embedded data\nQualtrics.SurveyEngine.setEmbeddedData(\'pageload_count\', pageload);\n\n});\n\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});\n\n\nQualtrics.SurveyEngine.addOnPageSubmit(function () {\n\t/*Place your JavaScript here to run when the participant clicks submit - the next button */\n\t\nvar qid = this.questionId;\nvar ht_audio_1 = String("${e://Field/ht_audio_1}")\nvar ht_audio_2 = String("${e://Field/ht_audio_2}")\nvar ht_audio_3 = String("${e://Field/ht_audio_3}")\nvar ht_audio_4 = String("${e://Field/ht_audio_4}")\nvar ht_audio_5 = String("${e://Field/ht_audio_5}")\nvar ht_audio_6 = String("${e://Field/ht_audio_6}")\n\n\nvar input_digits_1 = this.getChoiceValue(4, 1);\nvar input_digits_2 = this.getChoiceValue(4, 2);\nvar input_digits_3 = this.getChoiceValue(4, 3);\nvar input_digits_4 = this.getChoiceValue(4, 4);\nvar input_digits_5 = this.getChoiceValue(4, 5);\nvar input_digits_6 = this.getChoiceValue(4, 6);\n\nfunction regexEscape(str) {\n    return str.replace(/[-/\\\\^$*+?.()|[\\]{}]/g, \'\\\\$&\')\n}\n\n\n\nfunction getStringSimilarity(correct_digits, input_digits) {\n\tvar flags = \'g\';\n\tvar reg1 = "^\\\\d{0,2}["  + correct_digits + "]\\\\d{0,2}$";\n\tvar reg2 = "^\\\\d?" + correct_digits.substring(0,1) + "\\\\d?[" + correct_digits.substring(1,3) + "]\\\\d?$";\n\tvar reg3 = "^\\\\d?" + correct_digits.substring(1,2) + "\\\\d?" + correct_digits.substring(2,3) + "\\\\d?$";\n\tvar reg4 = "^"  + correct_digits + "$";\n\tvar similarity = 0;\n\t\n\tvar re1 = new RegExp(reg1, flags);\n\tvar re2 = new RegExp(reg2, flags);\n\tvar re3 = new RegExp(reg3, flags);\n\tvar re4 = new RegExp(reg4, flags);\n\t\n\tif (re1.test(input_digits)) {\n\t\tsimilarity += 1;\n\t};\n\t\n\tif ((re2.test(input_digits)) || (re3.test(input_digits))) {\n\t\tsimilarity += 1;\n\t}; \n\t\n\tif (re4.test(input_digits)) {\n\t\tsimilarity += 1;\n\t};\n\n  \treturn similarity;\n};\n\n\t\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q1\', getStringSimilarity(ht_audio_1, input_digits_1) );\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q2\', getStringSimilarity(ht_audio_2, input_digits_2) );\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q3\', getStringSimilarity(ht_audio_3, input_digits_3) );\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q4\', getStringSimilarity(ht_audio_4, input_digits_4) );\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q5\', getStringSimilarity(ht_audio_5, input_digits_5) );\nQualtrics.SurveyEngine.setEmbeddedData(\'ht_q6\', getStringSimilarity(ht_audio_6, input_digits_6) );\n\n\n\n});',
        "QuestionText": '<h1>&nbsp;</h1>\n\n<h1><b>Hearing Test</b></h1>\n\n<div>&nbsp;</div>\nPlease note that <strong>this is not a medical test</strong> but a quick method for us to check your acoustic environment, attention, hearing, and noise sensitivity. If you are worried about your hearing please consult a qualified doctor.&nbsp;\n\n<div>&nbsp;</div>\n\n<div>Please <strong>use headphones</strong> to listen to the following audio files and make sure you are <strong>in a quiet environment</strong>. If your headphones&#39; <strong>automatic noise cancellation</strong> is active, please make sure to disable it.</div>\n\n<div>&nbsp;</div>\n\n<div>In this test, you will hear speech in noise saying &quot;The digits&quot; followed by <strong>3 digits</strong>. Each digit is a random number between 0 and 9, where 0 is pronounced &quot;zero.&quot; Please listen carefully and type the three digits that you hear in the box provided below. If you are uncertain, please write your best guess about the 3 digits, or if you do not hear all of the 3 digits, write only those that you hear, for example: &quot;0&quot; or &quot;01&quot; or &quot;012&quot;.</div>\n\n<br>\n<br> \n<div class="notice">\n\t <strong>Important Notice:</strong> Only participants who pass correctly this hearing test <strong><u>will be eligible for additional bonus jobs</u></strong>. Please ensure you complete the test to qualify.\n</div>',
        "QuestionText_Unsafe": '<h1>&nbsp;</h1>\n\n<h1><b>Listening Test</b></h1>\n\n<div>&nbsp;</div>\nPlease note that <strong>this is not a medical test</strong> but a quick method for us to check your acoustic environment, attention, hearing, and noise sensitivity. If you are worried about your hearing please consult a qualified doctor.&nbsp;\n\n<div>&nbsp;</div>\n\n<div>Please <strong>use headphones</strong> to listen to the following audio files and make sure you are <strong>in a quiet environment</strong>. If your headphones\' <strong>automatic noise cancellation</strong> is active, please make sure to disable it.</div>\n\n<div>&nbsp;</div>\n\n<div>In this test, you will hear speech in noise saying "The digits" followed by <strong>3 digits</strong>. Each digit is a random number between 0 and 9, where 0 is pronounced "zero." Please listen carefully and type the three digits that you hear in the box provided below. If you are uncertain, please write your best guess about the 3 digits, or if you do not hear all of the 3 digits, write only those that you hear, for example: "0" or "01" or "012".</div>\n\n<br>\n<br> \n<div class="notice">\n\t <strong>Important Notice:</strong> Only participants who pass correctly this hearing test <strong><u>will be eligible for additional bonus jobs</u></strong>. Please ensure you complete the test to qualify.\n</div>',
        "QuestionType": "Matrix",
        "Randomization": {
            "Advanced": None,
            "ConsistentScaleReversal": True,
            "EvenPresentation": False,
            "TotalRandSubset": "",
            "Type": "All",
        },
        "RecodeValues": {"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6"},
        "Selector": "TE",
        "SubSelector": "Short",
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "CustomValidation",
                "MinChars": "1",
                "CustomValidation": {
                    "Logic": {
                        "0": {
                            "0": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/1",
                                "Description": '<span class="ConjDesc">If</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/1",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "1": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/2",
                                "Conjuction": "And",
                                "Description": '<span class="ConjDesc">And</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/2",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "2": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/3",
                                "Conjuction": "And",
                                "Description": '<span class="ConjDesc">And</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/3",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "3": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/4",
                                "Conjuction": "And",
                                "Description": '<span class="ConjDesc">And</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/4",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "4": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/5",
                                "Conjuction": "And",
                                "Description": '<span class="ConjDesc">And</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/5",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "5": {
                                "ChoiceLocator": "q://QID54/ChoiceTextEntryValue/4/6",
                                "Conjuction": "And",
                                "Description": '<span class="ConjDesc">And</span> <span class="QuestionDesc">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class="LeftOpDesc">Text Response</span> <span class="OpDesc">Matches Regex</span> <span class="RightOpDesc"> ^\\d{1,3}$ </span>',
                                "LeftOperand": "q://QID54/ChoiceTextEntryValue/4/6",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID54",
                                "QuestionIDFromLocator": "QID54",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression",
                            },
                            "Type": "If",
                        },
                        "Type": "BooleanExpression",
                    },
                    "Message": {
                        "description": "Error Text",
                        "libraryID": "UR_8ldtlrFg8W5ziES",
                        "messageID": "MS_d0c1t8cHvIjvxQi",
                        "subMessageID": "VE_ERROR",
                    },
                },
            }
        },
    },
}
