"""
Survey templates (code from the QSF file)
"""

TRAINING_QUESTION = {
    "SurveyID": "SV_e5Nwu5A6BgrJciy",
    "Element": "SQ",
    "PrimaryAttribute": "QID18",
    "SecondaryAttribute": "X / ${e://Field/total_training_questions} What word do you hear? \u00a0 \u00a0 \u00a0 \u00a0 \u00a0PLAY\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong>\n</strong></strong></div><strong><strong>\n\n<h3><br></h3><div><br></div><div style="text-align: center;"><h3>What word do you hear?</h3><br></div><div><br></div><div><br></div>\n\n<div style="text-align: center;"><button type="button" id="audiobutton1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;PLAY&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong></button></div>&nbsp;<audio src="AUDIO_LINK_PLACEHOLDER" id="audio1"></audio>\n&nbsp;<br>&nbsp; <br><br>',
        "DefaultChoices": False,
        "DataExportTag": "Q22",
        "QuestionType": "MC",
        "Selector": "SAHR",
        "SubSelector": "TX",
        "Configuration": {
            "QuestionDescriptionOption": "UseText",
            "LabelPosition": "BELOW",
        },
        "QuestionDescription": "X / ${e://Field/total_training_questions} What word do you hear? \u00a0 \u00a0 \u00a0 \u00a0 \u00a0PLAY\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0",
        "Choices": {"1": {"Display": "Target"}, "2": {"Display": "Alternative"}},
        "ChoiceOrder": [1, 2],
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
        "GradingData": [],
        "Language": {
            "AR": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="total-pages">${e://Field/total_training_questions}</span> / <span id="current-page">X</span><strong> </strong></strong></div>\n\n<h3 style=";"><strong><strong>\u00a0</strong></strong></h3>\n\n<div style=";"><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3 style=""><strong><strong>\u0645\u0627 \u0647\u064a \u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u062a\u064a \u062a\u0633\u0645\u0639\u0647\u0627\u061f</strong></strong></h3>\n</div>\n\n<div style=";"><strong><strong>\u00a0</strong></strong></div>\n\n<div style=";"><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><b id="docs-internal-guid-28ecfa1c-7fff-8360-02b1-2d29e8bbd0cb">\u062a\u0634\u063a\u064a\u0644</b></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "\u0647\u062f\u0641"},
                    "2": {"Display": "\u0628\u062f\u064a\u0644"},
                },
            },
            "DE": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>Welches Wort h\u00f6ren Sie?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>ABSPIELEN</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {"1": {"Display": "Ziel"}, "2": {"Display": "Alternative"}},
            },
            "ES": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>\u00bfQu\u00e9 palabra escuchas?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>REPRODUCIR</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "Objetivo"},
                    "2": {"Display": "Alternativa"},
                },
            },
            "FR": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>Quel mot entends-tu ?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>JOUER</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {"1": {"Display": "Cible"}, "2": {"Display": "Alternative"}},
            },
            "JA": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>\u3069\u3093\u306a\u8a00\u8449\u304c\u805e\u3053\u3048\u307e\u3059\u304b\uff1f</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><b id="docs-internal-guid-0d0c6b6f-7fff-5052-511c-06819346c7fc">\u00a0 \u00a0\u518d\u751f\u00a0\u00a0</b></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n\u00a0<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "\u76ee\u6a19"},
                    "2": {"Display": "\u5225"},
                },
            },
            "ZH-S": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_training_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong><b id="docs-internal-guid-021c72ee-7fff-ad35-d98f-eacf9c86eea3">\u60a8\u542c\u5230\u4ec0\u4e48\u5b57\u8bcd\uff1f</b></strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><b id="docs-internal-guid-05c98424-7fff-9d4e-a836-8893d61f0e6a">\u64ad\u653e</b></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "\u76ee\u6807"},
                    "2": {"Display": "\u9009\u62e9"},
                },
            },
        },
        "NextChoiceId": 3,
        "NextAnswerId": 1,
        "QuestionID": "QID18",
        "QuestionJS": '/*variables that came from setup survey*/\n\nvar trainValidationType = "TRAINING_TYPE_PLACEHOLDER"\n\nQualtrics.SurveyEngine.addOnload(function()\n{\n\t\n\t/*Place your JavaScript here to run when the page loads*/\n\t\n});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\t\n\t//This is the code related to the number of questions:\n\t\n\tlet simpleCounter = Number("$e{ e://Field/counter_training_questions + 1 }");\n\n\tQualtrics.SurveyEngine.setEmbeddedData(\'counter_training_questions\', simpleCounter);\n\t\n\tjQuery("#current-page").html(simpleCounter)\n\t\n\tjQuery("td").css("border-left","2px solid WhiteSmoke");\n\t\n\t\n\t\n\tjQuery("td").css("border-left","2px solid WhiteSmoke");\n\t\n\t\n\tvar mainElement = this\n\tthis.hidePreviousButton();\n\tthis.hideNextButton();\n\n\tvar label =  jQuery(".LabelWrapper")\n\tvar audio1 = document.getElementById("audio1");\n\tvar playcount1 = 0;\n\n\taudio1.volume = 1; //set audio volume to 1\n\tvar button1 =  document.getElementById("audiobutton1"); //grab button id\n\t\n\t\n\t\n\t//Function that triggers then you click over the question\n\tthis.questionclick = function(event, element) {\n\t\t\n\t\tif (this.getSelectedChoices().length > 0) {\n\t\t\t\tmainElement.showNextButton();\n\t\t}\n    }\n\t\n\t// CREATE playAudio() FUNCTION\n\tfunction playAudio1() {\n\t\t\n\t\tplaycount1++\n\t    audio1.play(); //play the audio one last time \n\t};\n\t\n\taudio1.onended = function() {\n\t\t\n\t\tvar buttonText = jQuery(\'#audiobutton1\').text();\n\t\t\n\t\tlabel.css("pointer-events","auto");\n\t\t\n\t\tjQuery("#audiobutton1").css(\'background-color\', \'#C9CAC9\');\n\t\tjQuery("#audiobutton1").prop(\'disabled\', true);\n\t\t\n\t\tif (buttonText.includes(\'PLAY\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;PLAYED&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'REPRODUCIR\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; REPRODUCIDO&nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'\u518d\u751f\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u518d\u751f\u6e08&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'\u64ad\u653e\')) {\n\t\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u5df2\u64ad\u653e&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'ABSPIELEN\')) {\n\t\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;ABGESPIELT&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'\u062a\u0634\u063a\u064a\u0644\')) {\n\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u0625\u0646\u062a\u0647\u0627\u0621 \u0627\u0644\u062a\u0634\u063a\u064a\u0644&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'JOUER\')) {\n\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;JOU\u00c9&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t}\n\n\t\t\n\t}; \n\n\t// TRIGGER playAudio() function on button press (note that the HTML element id for the button is called "audiobutton"\n\tjQuery("#audiobutton1").on("click", playAudio1);\n\n\t\n\tvar label =  jQuery(".LabelWrapper")\n\tlabel.css("pointer-events","none");\n\t\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});\n\nQualtrics.SurveyEngine.addOnPageSubmit(function () {\n\n\n\t//This functions are for incresing the value of the counters depending on the type of audio\n\t\n\t\n\tif (this.getChoices()[0] == this.getChoiceValue()){\n\n\t\n\t\tif (trainValidationType == "clean"){\n\t\t\tlet val1Counter = Number("$e{ e://Field/train_clean_counter + 1 }");\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\'train_clean_counter\', val1Counter);\n\t\t}\n\n\t\tif (trainValidationType == "noisy"){\n\t\t\tlet val2Counter = Number("$e{ e://Field/train_noisy_counter + 1 }");\n\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\'train_noisy_counter\', val2Counter);\n\t\t}\n\t\t\n\t}\n\t\n\t\n});',
        "Randomization": {"Advanced": None, "TotalRandSubset": "", "Type": "All"},
        "QuestionText_Unsafe": '<h3><br></h3><div><br></div><div style="text-align: center;"><h3>What word do you hear?</h3><br></div><div><br></div><div><br></div>\n\n<div style="text-align: center;"><button type="button" id="audiobutton1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;PLAY&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong></button></div>&nbsp;<audio src="AUDIO_LINK_PLACEHOLDER" id="audio1"></audio>\n&nbsp;<br>&nbsp; <br><br>',
        "DataVisibility": {"Private": False, "Hidden": False},
    },
}

TESTING_QUESTION = {
    "SurveyID": "SV_e5Nwu5A6BgrJciy",
    "Element": "SQ",
    "PrimaryAttribute": "QID24",
    "SecondaryAttribute": "X / ${e://Field/total_main_questions} What word do you hear? \u00a0 \u00a0 \u00a0 \u00a0 \u00a0PLAY\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 ",
    "TertiaryAttribute": None,
    "Payload": {
        "QuestionText": '<div style="position: relative; text-align: right;">\n  <strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong>\n</strong></strong></div><strong><strong>\n\n<h3><br></h3><div><br></div><div style="text-align: center;"><h3>What word do you hear?</h3><br></div><div><br></div><div><br></div>\n\n<div style="text-align: center;"><button type="button" id="audiobutton1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;PLAY&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong></button></div>&nbsp;<audio src="AUDIO_LINK_PLACEHOLDER" id="audio1"></audio>\n&nbsp;<br>&nbsp; <br><br>',
        "DefaultChoices": False,
        "DataExportTag": "Q25",
        "QuestionType": "MC",
        "Selector": "SAHR",
        "SubSelector": "TX",
        "Configuration": {
            "QuestionDescriptionOption": "UseText",
            "LabelPosition": "BELOW",
        },
        "QuestionDescription": "X / ${e://Field/total_main_questions} What word do you hear? \u00a0 \u00a0 \u00a0 \u00a0 \u00a0PLAY\u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0",
        "Choices": {"1": {"Display": "Target"}, "2": {"Display": "Alternate"}},
        "ChoiceOrder": [1, 2],
        "Validation": {
            "Settings": {
                "ForceResponse": "ON",
                "ForceResponseType": "ON",
                "Type": "None",
            }
        },
        "GradingData": [],
        "Language": {
            "AR": {
                "QuestionText": '<h3 style=";direction:rtl">\u00a0</h3>\n\n<div style=";direction:rtl">\u00a0</div>\n\n<div style="text-align: center;direction:rtl">\n<h3 style=";direction:rtl">\u0645\u0627 \u0647\u064a \u0627\u0644\u0643\u0644\u0645\u0629 \u0627\u0644\u062a\u064a \u062a\u0633\u0645\u0639\u0647\u0627\u061f</h3>\n</div>\n\n<div style=";direction:rtl">\u00a0</div>\n\n<div style=";direction:rtl">\u00a0</div>\n\n<div style="text-align: center;direction:rtl"><button id="audiobutton1" type="button"><b id="docs-internal-guid-28ecfa1c-7fff-8360-02b1-2d29e8bbd0cb">\u062a\u0634\u063a\u064a\u0644</b></button></div>\n\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0',
                "Choices": {
                    "1": {"Display": "\u0647\u062f\u0641"},
                    "2": {"Display": "\u0627\u0644\u0628\u062f\u064a\u0644"},
                },
            },
            "DE": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>Welches Wort h\u00f6ren Sie?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>ABSPIELEN</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {"1": {"Display": "Ziel"}, "2": {"Display": "Wechseln"}},
            },
            "ES": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>\u00bfQu\u00e9 palabra escuchas?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>REPRODUCIR</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {"1": {"Display": "Objetivo"}, "2": {"Display": "Alterno"}},
            },
            "FR": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>Quel mot entends-tu ?</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><strong>JOUER</strong></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {"1": {"Display": "Cible"}, "2": {"Display": "Alterner"}},
            },
            "JA": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong>\u3069\u3093\u306a\u8a00\u8449\u304c\u805e\u3053\u3048\u307e\u3059\u304b\uff1f</strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><b id="docs-internal-guid-0d0c6b6f-7fff-5052-511c-06819346c7fc">\u00a0 \u00a0 \u518d\u751f\u00a0 \u00a0\u00a0</b></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "\u76ee\u6a19"},
                    "2": {"Display": "\u4ee3\u308f\u308a\u306e"},
                },
            },
            "ZH-S": {
                "QuestionText": '<div style="position: relative; text-align: right;"><strong><span id="current-page">X</span> / <span id="total-pages">${e://Field/total_main_questions}</span><strong> </strong></strong></div>\n\n<h3><strong><strong>\u00a0</strong></strong></h3>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;">\n<h3><strong><strong><b id="docs-internal-guid-021c72ee-7fff-ad35-d98f-eacf9c86eea3">\u60a8\u542c\u5230\u4ec0\u4e48\u5b57\u8bcd\uff1f</b></strong></strong></h3>\n</div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div><strong><strong>\u00a0</strong></strong></div>\n\n<div style="text-align: center;"><strong><strong><button id="audiobutton1" type="button"><b id="docs-internal-guid-05c98424-7fff-9d4e-a836-8893d61f0e6a">\u64ad\u653e</b></button></strong></strong></div>\n<strong><strong>\n<audio id="audio1" src="AUDIO_LINK_PLACEHOLDER">\u00a0</audio>\n<br />\n<br />\n\u00a0</strong></strong>',
                "Choices": {
                    "1": {"Display": "\u76ee\u6807"},
                    "2": {"Display": "\u5907\u7528"},
                },
            },
        },
        "NextChoiceId": 3,
        "NextAnswerId": 1,
        "QuestionID": "QID24",
        "Randomization": {"Advanced": None, "TotalRandSubset": "", "Type": "All"},
        "QuestionJS": 'var isValidation = IS_VALIDATION_PLACEHOLDER\nvar mainValidationType = "TESTING_TYPE_PLACEHOLDER"\n\nQualtrics.SurveyEngine.addOnload(function()\n{\n\t\n\t/*Place your JavaScript here to run when the page loads*/\n\n\n});\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\t\n\t//This is the code related to the number of questions:\n\t\n\tlet simpleCounter = Number("$e{ e://Field/counter_main_questions + 1 }");\n\n\tQualtrics.SurveyEngine.setEmbeddedData(\'counter_main_questions\', simpleCounter);\n\t\n\tjQuery("#current-page").html(simpleCounter)\n\t\n\t\n\tjQuery("td").css("border-left","2px solid WhiteSmoke");\n\t\n\t\n\tvar mainElement = this\n\tthis.hidePreviousButton();\n\tthis.hideNextButton();\n\n\tvar label =  jQuery(".LabelWrapper")\n\tvar audio1 = document.getElementById("audio1");\n\tvar playcount1 = 0;\n\n\taudio1.volume = 1; //set audio volume to 1\n\tvar button1 =  document.getElementById("audiobutton1"); //grab button id\n\t\n\t//Function that triggers then you click over the question\n\tthis.questionclick = function(event, element) {\n\t\t\n\t\tif (this.getSelectedChoices().length > 0) {\n\t\t\t\tmainElement.showNextButton();\n\t\t}\n    }\n\t\n\t// CREATE playAudio() FUNCTION\n\tfunction playAudio1() {\n\t\t\n\t\tplaycount1++\n\t    audio1.play(); //play the audio one last time \n\t};\n\t\n\taudio1.onended = function() {\n\t\t\n\t\tvar buttonText = jQuery(\'#audiobutton1\').text();\n\t\t\n\t\tlabel.css("pointer-events","auto");\n\t\t\n\t\tjQuery("#audiobutton1").css(\'background-color\', \'#C9CAC9\');\n\t\tjQuery("#audiobutton1").prop(\'disabled\', true);\n\t\t\n\t\tif (buttonText.includes(\'PLAY\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;PLAYED&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'REPRODUCIR\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; REPRODUCIDO&nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'\u518d\u751f\')) {\n\t\t\t\n\t\t  \tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u518d\u751f\u6e08&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t} else if (buttonText.includes(\'\u64ad\u653e\')) {\n\t\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u5df2\u64ad\u653e&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'ABSPIELEN\')) {\n\t\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;ABGESPIELT&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'\u062a\u0634\u063a\u064a\u0644\')) {\n\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;\u0625\u0646\u062a\u0647\u0627\u0621 \u0627\u0644\u062a\u0634\u063a\u064a\u0644&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\n\t\t} else if (buttonText.includes(\'JOUER\')) {\n\t\t\n\t\t\tjQuery("#audiobutton1").html("<strong>&nbsp; &nbsp; &nbsp; &nbsp;JOU\u00c9&nbsp; &nbsp; &nbsp; &nbsp;</strong>");\n\t\t\t\n\t\t}\n\t\t\n\t\t\n\t}; \n\n\t// TRIGGER playAudio() function on button press (note that the HTML element id for the button is called "audiobutton"\n\tjQuery("#audiobutton1").on("click", playAudio1);\n\n\t\n\tvar label =  jQuery(".LabelWrapper")\n\tlabel.css("pointer-events","none");\n\t\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});\n\nQualtrics.SurveyEngine.addOnPageSubmit(function () {\n\n\n\t//This functions are for incresing the value of the counters depending on the type of audio\n\t\n\tif (isValidation == true){\n\n\t\tif (this.getChoices()[0] == this.getChoiceValue()){\n\n\n\t\t\tif (mainValidationType == "clean"){\n\t\t\t\tlet val1Counter = Number("$e{ e://Field/main_clean_counter + 1 }");\n\t\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\'main_clean_counter\', val1Counter);\n\t\t\t}\n\n\t\t\tif (mainValidationType == "noisy"){\n\t\t\t\tlet val2Counter = Number("$e{ e://Field/main_noisy_counter + 1 }");\n\t\t\t\tQualtrics.SurveyEngine.setEmbeddedData(\'main_noisy_counter\', val2Counter);\n\t\t\t}\n\n\t\t}\n\n\t}\n\t\n\t\n});',
        "QuestionText_Unsafe": '<h3><br></h3><div><br></div><div style="text-align: center;"><h3>What word do you hear?</h3><br></div><div><br></div><div><br></div>\n\n<div style="text-align: center;"><button type="button" id="audiobutton1"><strong>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;PLAY&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</strong></button></div>&nbsp;<audio src="AUDIO_LINK_PLACEHOLDER" id="audio1"></audio>\n&nbsp;<br>&nbsp; <br><br>',
        "DataVisibility": {"Private": False, "Hidden": False},
    },
}

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

HEARING_TEST_TEMPLATE = {
    "SurveyID": "SV_e5Nwu5A6BgrJciy",
    "Element": "SQ",
    "PrimaryAttribute": "QID1213622116",
    "SecondaryAttribute": "\u00a0 Hearing Test \u00a0 Please note that this is not a medical test but a quick method for us to check y.",
    "TertiaryAttribute": None,
    "Payload": {
        "AnswerOrder": [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6"
        ],
        "AnswerRandomization": {
            "Advanced": None,
            "TotalRandSubset": "",
            "Type": "All"
        },
        "Answers": {
            "1": {
                "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>"
            },
            "2": {
                "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>\n"
            },
            "3": {
                "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>\n"
            },
            "4": {
                "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>\n"
            },
            "5": {
                "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>\n"
            },
            "6": {
                "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">&nbsp;</audio>\n"
            }
        },
        "ChoiceDataExportTags": False,
        "ChoiceOrder": [
            "4"
        ],
        "Choices": {
            "4": {
                "Display": "Digits:"
            }
        },
        "Configuration": {
            "ChoiceColumnWidth": 25,
            "MobileFirst": True,
            "QuestionDescriptionOption": "UseText",
            "RepeatHeaders": "none",
            "TextPosition": "inline",
            "ChoiceColumnWidthPixels": 72
        },
        "DataVisibility": {
            "Hidden": False,
            "Private": False
        },
        "DefaultChoices": False,
        "GradingData": [],
        "Language": {
            "AR": {
                "QuestionText": "<h1 style=\";text-align:right;direction:rtl\">\u00a0</h1>\n\n<h1 style=\";text-align:right;direction:rtl\"><b>\u0627\u062e\u062a\u0628\u0627\u0631 \u0627\u0644\u0633\u0645\u0639</b></h1>\n\n<div style=\";text-align:right;direction:rtl\">\u00a0</div>\n\n<p dir=\"ltr\"><b id=\"docs-internal-guid-ec6f23c8-7fff-eef4-0af4-cba19e0cb128\">\u064a</b>\u0631\u062c\u0649 \u0645\u0644\u0627\u062d\u0638\u0629 \u0623\u0646 \u0647\u0630\u0627 \u0644\u064a\u0633 \u0627\u062e\u062a\u0628\u0627\u0631\u064b\u0627 \u0637\u0628\u064a\u064b\u0627 \u0648\u0644\u0643\u0646\u0647 \u0637\u0631\u064a\u0642\u0629 \u0633\u0631\u064a\u0639\u0629 \u0628\u0627\u0644\u0646\u0633\u0628\u0629 \u0644\u0646\u0627 \u0644\u0644\u062a\u062d\u0642\u0642 \u0645\u0646 \u0627\u0644\u0628\u064a\u0626\u0629 \u0627\u0644\u0635\u0648\u062a\u064a\u0629 \u0648\u0627\u0644\u0627\u0646\u062a\u0628\u0627\u0647 \u0648\u0627\u0644\u0633\u0645\u0639 \u0648\u062d\u0633\u0627\u0633\u064a\u0629 \u0627\u0644\u0636\u0648\u0636\u0627\u0621. \u0625\u0630\u0627 \u0643\u0646\u062a \u0642\u0644\u0642\u064b\u0627 \u0628\u0634\u0623\u0646 \u0633\u0645\u0639\u0643 \u060c \u0641\u064a\u0631\u062c\u0649 \u0627\u0633\u062a\u0634\u0627\u0631\u0629 \u0637\u0628\u064a\u0628 \u0645\u0624\u0647\u0644.<b>\u00a0</b></p>\n<br />\n\u064a\u0631\u062c\u0649 \u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0633\u0645\u0627\u0639\u0627\u062a \u0627\u0644\u0631\u0623\u0633 \u0637\u0648\u0627\u0644 \u0627\u0644\u0645\u0647\u0645\u0629 \u0628\u0623\u0643\u0645\u0644\u0647\u0627 \u060c \u0648\u062a\u0623\u0643\u062f \u0645\u0646 \u0623\u0646\u0643 \u0641\u064a \u0628\u064a\u0626\u0629 \u0647\u0627\u062f\u0626\u0629. \u0625\u0630\u0627 \u0643\u0627\u0646 \u0625\u0644\u063a\u0627\u0621 \u0627\u0644\u0636\u0648\u0636\u0627\u0621 \u0627\u0644\u062a\u0644\u0642\u0627\u0626\u064a \u0641\u064a \u0633\u0645\u0627\u0639\u0627\u062a \u0627\u0644\u0631\u0623\u0633 \u0646\u0634\u0637\u064b\u0627 \u060c \u0641\u064a\u0631\u062c\u0649 \u0627\u0644\u062a\u0623\u0643\u062f \u0645\u0646 \u062a\u0639\u0637\u064a\u0644\u0647.\n<div style=\";text-align:right;direction:rtl\">\u00a0</div>\n\n<div style=\";text-align:right;direction:rtl\">\u0641\u064a \u0647\u0630\u0627 \u0627\u0644\u0627\u062e\u062a\u0628\u0627\u0631 \u060c \u0633\u0648\u0641 \u062a\u0633\u0645\u0639 \u0643\u0644\u0627\u0645\u064b\u0627 \u0641\u064a \u0636\u0648\u0636\u0627\u0621 \u064a\u0642\u0648\u0644 \"\u0627\u0644\u0623\u0631\u0642\u0627\u0645\" \u0645\u062a\u0628\u0648\u0639\u064b\u0627 \u0628\u0640 <strong>3 \u0623\u0631\u0642\u0627\u0645</strong> . \u0643\u0644 \u0631\u0642\u0645 \u0647\u0648 \u0631\u0642\u0645 \u0639\u0634\u0648\u0627\u0626\u064a \u0628\u064a\u0646 0 \u0648 9 \u060c \u062d\u064a\u062b \u064a\u062a\u0645 \u0646\u0637\u0642 0 \"\u0635\u0641\u0631\". \u064a\u0631\u062c\u0649 \u0627\u0644\u0627\u0633\u062a\u0645\u0627\u0639 \u0628\u0639\u0646\u0627\u064a\u0629 \u0648\u0643\u062a\u0627\u0628\u0629 \u0627\u0644\u0623\u0631\u0642\u0627\u0645 \u0627\u0644\u062b\u0644\u0627\u062b\u0629 \u0627\u0644\u062a\u064a \u062a\u0633\u0645\u0639\u0647\u0627 \u0641\u064a \u0627\u0644\u0645\u0631\u0628\u0639 \u0623\u062f\u0646\u0627\u0647. \u0625\u0630\u0627 \u0644\u0645 \u062a\u0643\u0646 \u0645\u062a\u0623\u0643\u062f\u064b\u0627 \u060c \u0641\u064a\u0631\u062c\u0649 \u0643\u062a\u0627\u0628\u0629 \u0623\u0641\u0636\u0644 \u062a\u062e\u0645\u064a\u0646 \u0644\u062f\u064a\u0643 \u0628\u0634\u0623\u0646 \u0627\u0644\u0623\u0631\u0642\u0627\u0645 \u0627\u0644\u062b\u0644\u0627\u062b\u0629 \u060c \u0623\u0648 \u0625\u0630\u0627 \u0644\u0645 \u062a\u0633\u0645\u0639 \u0643\u0644 \u0627\u0644\u0623\u0631\u0642\u0627\u0645 \u0627\u0644\u062b\u0644\u0627\u062b\u0629 \u060c \u0641\u0627\u0643\u062a\u0628 \u0641\u0642\u0637 \u0627\u0644\u0623\u0631\u0642\u0627\u0645 \u0627\u0644\u062a\u064a \u062a\u0633\u0645\u0639\u0647\u0627 \u060c \u0639\u0644\u0649 \u0633\u0628\u064a\u0644 \u0627\u0644\u0645\u062b\u0627\u0644: \"0\" \u0623\u0648 \"01\" \u0623\u0648 \"012\".</div>\n",
                "Choices": {
                    "4": {
                        "Display": "\u0623\u0631\u0642\u0627\u0645:"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            },
            "DE": {
                "QuestionText": "<h1>\u00a0</h1>\n\n<h1><b>H\u00f6rtest</b></h1>\n\n<div>\u00a0</div>\nBitte beachten Sie, dass <strong>dies kein medizinischer Test ist,</strong> sondern eine schnelle Methode, mit der wir Ihr akustisches Umfeld, Ihre Aufmerksamkeit, Ihr Geh\u00f6r und Ihre Ger\u00e4uschempfindlichkeit \u00fcberpr\u00fcfen k\u00f6nnen. Wenn Sie sich Sorgen um Ihr Geh\u00f6r machen, wenden Sie sich bitte an einen qualifizierten Arzt.<br />\n<br />\nBitte verwenden Sie w\u00e4hrend der gesamten Aufgabe Kopfh\u00f6rer und sorgen Sie f\u00fcr eine ruhige Umgebung. Falls Ihre Kopfh\u00f6rer \u00fcber eine Noise-Cancelling-Funktion verf\u00fcgen, deaktivieren Sie diese bitte.\n<div>\u00a0</div>\n\n<div>In diesem Test h\u00f6ren Sie gesprochene Ziffern in St\u00f6rrauschen. Der Sprecher beginnt den Satz mit den Worten \u201eDie Ziffern\u201c, gefolgt von <strong>3 Ziffern</strong>. Jede Ziffer ist eine Zufallszahl zwischen 0 und 9. Bitte h\u00f6ren Sie genau zu und geben Sie die drei Ziffern, die Sie h\u00f6ren, in das untenstehende Feld ein. Wenn Sie unsicher sind, schreiben Sie bitte Ihre beste Vermutung zu den 3 Ziffern, oder wenn Sie nicht alle 3 Ziffern h\u00f6ren, schreiben Sie nur die, die Sie h\u00f6ren, zum Beispiel: \u201e0\u201c oder \u201e01\u201c oder \u201e012\u201c.</div>\n",
                "Choices": {
                    "4": {
                        "Display": "Ziffern:"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            },
            "ES": {
                "QuestionText": "<h1>\u00a0</h1>\n\n<h1><b>Prueba de audici\u00f3n</b></h1>\n\n<div>\u00a0</div>\nTenga en cuenta que <strong>esta no es una prueba m\u00e9dica,</strong> sino un m\u00e9todo r\u00e1pido para que podamos verificar su entorno ac\u00fastico, atenci\u00f3n, audici\u00f3n y sensibilidad al ruido. Si le preocupa su audici\u00f3n, consulte a un m\u00e9dico cualificado.<br />\n<br />\nUtilice auriculares durante toda la tarea y aseg\u00farese de estar en un entorno tranquilo. Si la cancelaci\u00f3n autom\u00e1tica de ruido de sus auriculares est\u00e1 activa, aseg\u00farese de desactivarla.\n<div>\u00a0</div>\n\n<div>En esta prueba, escuchar\u00e1 hablar en ruido diciendo \"Los d\u00edgitos\" seguido de <strong>3 d\u00edgitos</strong> . Cada d\u00edgito es un n\u00famero aleatorio entre 0 y 9, donde 0 se pronuncia \"cero\". Escuche atentamente y escriba los tres d\u00edgitos que escucha en el cuadro que se proporciona a continuaci\u00f3n. Si no est\u00e1 seguro, escriba su mejor suposici\u00f3n sobre los 3 d\u00edgitos, o si no escucha todos los 3 d\u00edgitos, escriba solo los que escucha, por ejemplo: \"0\" o \"01\" o \"012\".</div>\n",
                "Choices": {
                    "4": {
                        "Display": "D\u00edgitos:"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            },
            "FR": {
                "QuestionText": "<h1>\u00a0</h1>\n\n<h1><b>Test auditif</b></h1>\n\n<div>\u00a0</div>\nVeuillez noter qu'il <strong>ne s'agit pas d'un test m\u00e9dical</strong> mais d'une m\u00e9thode rapide pour v\u00e9rifier votre environnement acoustique, votre attention, votre audition et votre sensibilit\u00e9 au bruit. Si vous vous inqui\u00e9tez pour votre audition, veuillez consulter un m\u00e9decin qualifi\u00e9.<br />\n<br />\nVeuillez utiliser des \u00e9couteurs tout au long de la t\u00e2che et assurez-vous d'\u00eatre dans un environnement calme. Si la suppression automatique du bruit de votre casque est active, assurez-vous de la d\u00e9sactiver.\n<div>\u00a0</div>\n\n<div>Dans ce test, vous entendrez une voix dans le bruit de fond disant \"Les chiffres\" suivi de <strong>3 chiffres</strong> . Chaque chiffre est un nombre al\u00e9atoire compris entre 0 et 9, o\u00f9 0 se prononce \"z\u00e9ro\". Veuillez \u00e9couter attentivement et taper les trois chiffres que vous entendez dans la case ci-dessous. Si vous n'\u00eates pas s\u00fbr, veuillez \u00e9crire votre meilleure supposition sur les 3 chiffres, ou si vous n'entendez pas tous les 3 chiffres, \u00e9crivez uniquement ceux que vous entendez, par exemple : \"0\" ou \"01\" ou \"012\".</div>\n",
                "Choices": {
                    "4": {
                        "Display": "Chiffres\u00a0:"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            },
            "JA": {
                "QuestionText": "<h1>\u00a0</h1>\n\n<h1><b>\u8074\u529b\u691c\u67fb</b></h1>\n\n<div><b id=\"docs-internal-guid-35cb3f8b-7fff-9621-7541-933eb0984fb9\">\u3053\u308c\u306f\u533b\u5b66\u7684\u691c\u67fb\u3067\u306f\u306a\u304f\u3001\u97f3\u97ff\u74b0\u5883\u3001\u6ce8\u610f\u529b\u3001\u8074\u529b\u3001\u304a\u3088\u3073\u9a12\u97f3\u611f\u5ea6\u3092\u78ba\u8a8d\u3059\u308b\u305f\u3081\u306e\u7c21\u5358\u306a\u65b9\u6cd5\u3067\u3042\u308b</b>\u3053\u3068\u3092\u3054\u7406\u89e3\u304f\u3060\u3055\u3044\u3002\u8074\u899a\u306b\u4e0d\u5b89\u304c\u3042\u308b\u5834\u5408\u306f\u3001\u5c02\u9580\u306e\u533b\u5e2b\u306b\u3054\u76f8\u8ac7\u304f\u3060\u3055\u3044\u3002<br />\n<br />\n\u30bf\u30b9\u30af\u5168\u4f53\u3092\u901a\u3057\u3066\u30d8\u30c3\u30c9\u30db\u30f3\u3092\u4f7f\u7528\u3057\u3001\u5fc5\u305a\u9759\u304b\u306a\u74b0\u5883\u3067\u884c\u3063\u3066\u304f\u3060\u3055\u3044\u3002\u30d8\u30c3\u30c9\u30db\u30f3\u306e\u81ea\u52d5\u30ce\u30a4\u30ba\u30ad\u30e3\u30f3\u30bb\u30ea\u30f3\u30b0\u6a5f\u80fd\u304c\u6709\u52b9\u306b\u306a\u3063\u3066\u3044\u308b\u5834\u5408\u306f\u3001\u5fc5\u305a\u7121\u52b9\u306b\u3057\u3066\u304f\u3060\u3055\u3044\u3002<br />\n<br />\n\u3053\u306e\u30c6\u30b9\u30c8\u3067\u306f\u3001\u96d1\u97f3\u306e\u4e2d\u3067\u300c\u6570\u5b57\u300d\u306e\u5f8c\u306b<strong>3 \u6841\u306e\u6570\u5b57\u306e</strong>\u97f3\u58f0\u304c\u805e\u3053\u3048\u307e\u3059\u3002\u5404\u6841\u306f 0 \uff5e 9 \u306e\u4e71\u6570\u3067\u30010 \u306f\u300c\u30bc\u30ed\u300d\u3068\u767a\u97f3\u3055\u308c\u307e\u3059\u3002\u3088\u304f\u805e\u3044\u3066\u3001\u805e\u3053\u3048\u305f 3 \u6841\u306e\u6570\u5b57\u3092\u4e0b\u306e\u30dc\u30c3\u30af\u30b9\u306b\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002\u3088\u304f\u308f\u304b\u3089\u306a\u3044\u5834\u5408\u306f\u3001\u6700\u3082\u6b63\u3057\u3044\u3068\u601d\u308f\u308c\u308b3\u6841\u306e\u6570\u5b57\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u30023 \u6841\u3059\u3079\u3066\u304c\u805e\u3053\u3048\u306a\u3044\u5834\u5408\u306f\u3001\u805e\u3053\u3048\u308b\u6570\u5b57\u3060\u3051\u3092\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002\u305f\u3068\u3048\u3070\u3001\u300c0\u300d\u3001\u300c01\u300d\u3001\u300c012\u300d\u306a\u3069\u3067\u3059\u3002</div>\n",
                "Choices": {
                    "4": {
                        "Display": "\u6570\u5b57:"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<strong><button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n</strong>"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play<br />\n</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play<br />\n</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            },
            "ZH-S": {
                "QuestionText": "<h1>\u00a0</h1>\n\n<h1><b>\u542c\u529b\u6d4b\u8bd5</b></h1>\n\n<div>\u00a0</div>\n\u8bf7\u6ce8\u610f\uff0c<strong>\u8fd9\u4e0d\u662f\u4e00\u9879\u533b\u5b66\u65b9\u9762\u7684\u6d4b\u8bd5</strong>\uff0c\u800c\u662f\u6211\u4eec\u7528\u6765\u5feb\u901f\u68c0\u67e5\u60a8\u7684\u58f0\u97f3\u73af\u5883\u3001\u6ce8\u610f\u529b\u3001\u542c\u529b\u548c\u566a\u97f3\u654f\u611f\u5ea6\u7684\u65b9\u6cd5\u3002\u5982\u679c\u60a8\u62c5\u5fc3\u81ea\u5df1\u7684\u542c\u529b\uff0c\u8bf7\u54a8\u8be2\u4e13\u4e1a\u533b\u751f\u3002<br />\n\u00a0\n<div>\u8bf7\u5728\u6574\u4e2a\u4efb\u52a1\u8fc7\u7a0b\u4e2d\u4f7f\u7528\u5934\u6234\u5f0f\u8033\u673a\uff0c\u5e76\u786e\u4fdd\u60a8\u5904\u4e8e\u5b89\u9759\u7684\u73af\u5883\u4e2d\u3002\u5982\u679c\u60a8\u7684\u8033\u673a\u5df2\u5f00\u542f\u81ea\u52a8\u964d\u566a\u529f\u80fd\uff0c\u8bf7\u786e\u4fdd\u7981\u7528\u8be5\u529f\u80fd\u3002<br />\n\u00a0</div>\n\n<div>\u5728\u6b64\u6d4b\u8bd5\u4e2d\uff0c\u60a8\u5c06\u542c\u5230\u5608\u6742\u73af\u5883\u4e2d\u7684\u8bed\u97f3\u8bf4\u201c\u6570\u5b57\u201d\uff0c\u7136\u540e\u62a5\u51fa\u4e09<strong>\u4e2a\u6570\u5b57</strong>\u3002\u6bcf\u4e2a\u6570\u5b57\u90fd\u662f 0 \u5230 9 \u4e4b\u95f4\u7684\u968f\u673a\u6570\uff0c\u5176\u4e2d 0 \u53d1\u97f3\u4e3a\u201c\u96f6\u201d\u3002\u8bf7\u4ed4\u7ec6\u8046\u542c\u5e76\u5728\u4e0b\u9762\u63d0\u4f9b\u7684\u8f93\u5165\u6846\u4e2d\u952e\u5165\u60a8\u542c\u5230\u7684\u4e09\u4e2a\u6570\u5b57\u3002\u5982\u679c\u60a8\u4e0d\u786e\u5b9a\uff0c\u8bf7\u5c3d\u91cf\u731c\u6d4b\u5e76\u952e\u5165\u4e09\u4e2a\u6570\u5b57\uff1b\u5982\u679c\u60a8\u6ca1\u6709\u542c\u6e05\u5168\u90e8\u4e09\u4e2a\u6570\u5b57\uff0c\u8bf7\u53ea\u5199\u4e0b\u60a8\u542c\u5230\u7684\u90a3\u51e0\u4e2a\u6570\u5b57\uff0c\u4f8b\u5982\uff1a\u201c0\u201d\uff0c\u6216\u201c01\u201d\uff0c\u6216\u201c012\u201d\u3002</div>\n",
                "Choices": {
                    "4": {
                        "Display": "\u6570\u5b57\uff1a"
                    }
                },
                "Answers": {
                    "1": {
                        "Display": "<button id=\"audiobutton1\" type=\"button\">Play</button>\n<audio id=\"audiofile1\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "2": {
                        "Display": "<button id=\"audiobutton2\" type=\"button\">Play</button>\n<audio id=\"audiofile2\" src=\"AUDIO_LINK_PLACEHOLDER\"><b id=\"docs-internal-guid-05c98424-7fff-9d4e-a836-8893d61f0e6a\">\u64ad\u653e</b><b id=\"docs-internal-guid-b55d112a-7fff-da70-15f9-e4c5c55002e3\">\u64ad\u653e</b></audio>\n"
                    },
                    "3": {
                        "Display": "<button id=\"audiobutton3\" type=\"button\">Play</button>\n<audio id=\"audiofile3\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "4": {
                        "Display": "<button id=\"audiobutton4\" type=\"button\">Play</button>\n<audio id=\"audiofile4\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "5": {
                        "Display": "<button id=\"audiobutton5\" type=\"button\">Play</button>\n<audio id=\"audiofile5\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    },
                    "6": {
                        "Display": "<button id=\"audiobutton6\" type=\"button\">Play</button>\n<audio id=\"audiofile6\" src=\"AUDIO_LINK_PLACEHOLDER\">\u00a0</audio>\n"
                    }
                }
            }
        },
        "NextAnswerId": 7,
        "NextChoiceId": 5,
        "QuestionDescription": "\u00a0 Hearing Test \u00a0 Please note that this is not a medical test but a quick method for us to check y...",
        "QuestionJS": "Qualtrics.SurveyEngine.addOnload(function()\n{\n\tthis.hidePreviousButton();\n\tthis.hideNextButton();\n\t//create variable to track play count\n\tvar playcount1 = 0; \n\tvar playcount2 = 0; \n\tvar playcount3 = 0; \n\tvar playcount4 = 0; \n\tvar playcount5 = 0; \n\tvar playcount6 = 0; \n\t//create variable to track page refresh count \n\tvar refreshcount = 0;\n\t//Get audio element\n\t//name \"audiofile1\" this whatever you name your audio element ID is within your HTML \n\tvar audio1 = document.getElementById(\"audiofile1\"); \n\tvar audio2 = document.getElementById(\"audiofile2\"); \n\tvar audio3 = document.getElementById(\"audiofile3\"); \n\tvar audio4 = document.getElementById(\"audiofile4\"); \n\tvar audio5 = document.getElementById(\"audiofile5\"); \n\tvar audio6 = document.getElementById(\"audiofile6\"); \n\taudio1.volume = 1; //set audio volume to 1\n\taudio2.volume = 1; //set audio volume to 1\n\taudio3.volume = 1; //set audio volume to 1\n\taudio4.volume = 1; //set audio volume to 1\n\taudio5.volume = 1; //set audio volume to 1\n\taudio6.volume = 1; //set audio volume to 1\n\tvar button1 = document.getElementById(\"audiobutton1\"); //grab button id\n\tvar button2 = document.getElementById(\"audiobutton2\"); //grab button id\n\tvar button3 = document.getElementById(\"audiobutton3\"); //grab button id\n\tvar button4 = document.getElementById(\"audiobutton4\"); //grab button id\n\tvar button5 = document.getElementById(\"audiobutton5\"); //grab button id\n\tvar button6 = document.getElementById(\"audiobutton6\"); //grab button id\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count1\", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count2\", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count3\", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count4\", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count5\", 0);\n\tQualtrics.SurveyEngine.setEmbeddedData(\"play_count6\", 0);\n\t\n// CREATE playAudio() FUNCTION\nfunction playAudio1() {\n  playcount1++; //increase playcount number by 1\n  console.log(playcount1); \n  audio1.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count1\", playcount1); \n};\n\nfunction playAudio2() {\n  playcount2++; //increase playcount number by 1\n  console.log(playcount2); \n  audio2.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count2\", playcount2); \n};\n\nfunction playAudio3() {\n  playcount3++; //increase playcount number by 1\n  console.log(playcount3); \n  audio3.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count3\", playcount3); \n};\n\t\nfunction playAudio4() {\n  playcount4++; //increase playcount number by 1\n  console.log(playcount4); \n  audio4.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count4\", playcount4); \n};\n\nfunction playAudio5() {\n  playcount5++; //increase playcount number by 1\n  console.log(playcount5); \n  audio5.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count5\", playcount5); \n};\n\t\nfunction playAudio6() {\n  playcount6++; //increase playcount number by 1\n  console.log(playcount6); \n  audio6.play(); //play the audio one last time \n   //update play_count embedded data to current playcount number \n  Qualtrics.SurveyEngine.setEmbeddedData(\"play_count6\", playcount6); \n};\n\t\naudio1.onended = function() {\n\tif (playcount1 < 5){\n\t\tbutton1.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton1.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\t\naudio2.onended = function() {\n\tif (playcount2 < 5){\n\t\tbutton2.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton2.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\t\naudio3.onended = function() {\n\tif (playcount3 < 5){\n\t\tbutton3.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton3.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\t\naudio4.onended = function() {\n\tif (playcount4 < 5){\n\t\tbutton4.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton4.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\t\naudio5.onended = function() {\n\tif (playcount5 < 5){\n\t\tbutton5.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton5.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\naudio6.onended = function() {\n\tif (playcount6 < 5){\n\t\tbutton6.style.visibility = \"visible\"; //show button again\n\t} else {\n\t\tbutton6.style.visibility = \"hidden\"; //hide the button so that it can't be played anymore\n\t}\n}; \n\n// TRIGGER playAudio() function on button press (note that the HTML element id for the button is called \"audiobutton\"\njQuery(\"#audiobutton1\").on(\"click\", playAudio1);\njQuery(\"#audiobutton2\").on(\"click\", playAudio2);\njQuery(\"#audiobutton3\").on(\"click\", playAudio3);\njQuery(\"#audiobutton4\").on(\"click\", playAudio4);\njQuery(\"#audiobutton5\").on(\"click\", playAudio5);\njQuery(\"#audiobutton6\").on(\"click\", playAudio6);\n\n\n// TRACKING PAGE REFRESH\n// NOTE: \"playcount\" variable refreshs to 0 if a respondent refreshes the page\n\t// WARNING: The three lines below will not work properly if this JavaScript is on the first page of the survey\n\t\n// Pull number in pageload (default within embedded data element should be set to 0)\nvar pageload = Qualtrics.SurveyEngine.getEmbeddedData('pageload_count');\npageload = parseInt(pageload)+1; \n//save updated reload value to 'refresh_count' embedded data\nQualtrics.SurveyEngine.setEmbeddedData('pageload_count', pageload);\n\n});\n\n\nQualtrics.SurveyEngine.addOnReady(function()\n{\n\t/*Place your JavaScript here to run when the page is fully displayed*/\n\tvar mainElement = this\n\t\n\tjQuery(\"input[type='text']\").attr(\"autocomplete\", \"off\");\n\tvar $textInputs = jQuery('input[type=\"text\"]');\n\t$textInputs.on('input', function () {\n\t\t// Initialize a variable to track whether all inputs have content\n\t\tvar allInputsHaveContent = true;\n\n\t\t// Loop through each text input and check if it's empty\n\t\t$textInputs.each(function () {\n\t\t\tif (jQuery(this).val().trim() === '') {\n\t\t\t\tallInputsHaveContent = False;\n\t\t\t\treturn False; // Exit the loop early if one input is empty\n\t\t\t}\n\t\t});\n\n\t\t// Check if all inputs have content and trigger your function if true\n\t\tif (allInputsHaveContent) {\n\t\t\tmainElement.showNextButton();\n\t\t}\n\t\t\n\t});\n\t\t\t\t\t\t\n\n\n\n});\n\nQualtrics.SurveyEngine.addOnUnload(function()\n{\n\t/*Place your JavaScript here to run when the page is unloaded*/\n\n});\n\n\nQualtrics.SurveyEngine.addOnPageSubmit(function () {\n\t/*Place your JavaScript here to run when the participant clicks submit - the next button */\n\t\nvar qid = this.questionId;\nvar ht_audio_1 = String(\"${e://Field/ht_audio_1}\")\nvar ht_audio_2 = String(\"${e://Field/ht_audio_2}\")\nvar ht_audio_3 = String(\"${e://Field/ht_audio_3}\")\nvar ht_audio_4 = String(\"${e://Field/ht_audio_4}\")\nvar ht_audio_5 = String(\"${e://Field/ht_audio_5}\")\nvar ht_audio_6 = String(\"${e://Field/ht_audio_6}\")\n\n\nvar input_digits_1 = this.getChoiceValue(4, 1);\nvar input_digits_2 = this.getChoiceValue(4, 2);\nvar input_digits_3 = this.getChoiceValue(4, 3);\nvar input_digits_4 = this.getChoiceValue(4, 4);\nvar input_digits_5 = this.getChoiceValue(4, 5);\nvar input_digits_6 = this.getChoiceValue(4, 6);\n\nfunction regexEscape(str) {\n    return str.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&')\n}\n\n\n\nfunction getStringSimilarity(correct_digits, input_digits) {\n\tvar flags = 'g';\n\tvar reg1 = \"^\\\\d{0,2}[\"  + correct_digits + \"]\\\\d{0,2}$\";\n\tvar reg2 = \"^\\\\d?\" + correct_digits.substring(0,1) + \"\\\\d?[\" + correct_digits.substring(1,3) + \"]\\\\d?$\";\n\tvar reg3 = \"^\\\\d?\" + correct_digits.substring(1,2) + \"\\\\d?\" + correct_digits.substring(2,3) + \"\\\\d?$\";\n\tvar reg4 = \"^\"  + correct_digits + \"$\";\n\tvar similarity = 0;\n\t\n\tvar re1 = new RegExp(reg1, flags);\n\tvar re2 = new RegExp(reg2, flags);\n\tvar re3 = new RegExp(reg3, flags);\n\tvar re4 = new RegExp(reg4, flags);\n\t\n\tif (re1.test(input_digits)) {\n\t\tsimilarity += 1;\n\t};\n\t\n\tif ((re2.test(input_digits)) || (re3.test(input_digits))) {\n\t\tsimilarity += 1;\n\t}; \n\t\n\tif (re4.test(input_digits)) {\n\t\tsimilarity += 1;\n\t};\n\n  \treturn similarity;\n};\n\n\t\nQualtrics.SurveyEngine.setEmbeddedData('ht_q1', getStringSimilarity(ht_audio_1, input_digits_1) );\nQualtrics.SurveyEngine.setEmbeddedData('ht_q2', getStringSimilarity(ht_audio_2, input_digits_2) );\nQualtrics.SurveyEngine.setEmbeddedData('ht_q3', getStringSimilarity(ht_audio_3, input_digits_3) );\nQualtrics.SurveyEngine.setEmbeddedData('ht_q4', getStringSimilarity(ht_audio_4, input_digits_4) );\nQualtrics.SurveyEngine.setEmbeddedData('ht_q5', getStringSimilarity(ht_audio_5, input_digits_5) );\nQualtrics.SurveyEngine.setEmbeddedData('ht_q6', getStringSimilarity(ht_audio_6, input_digits_6) );\n\n\n\n});",
        "QuestionText": "<h1>&nbsp;</h1>\n\n<h1><b>Hearing Test</b></h1>\n\n<div>&nbsp;</div>\nPlease note that <strong>this is not a medical test</strong> but a quick method for us to check your acoustic environment, attention, hearing, and noise sensitivity. If you are worried about your hearing please consult a qualified doctor.&nbsp;\n\n<br><br>Please use headphones throughout the entire task, and make sure you are in a quiet environment. If your headphones' automatic noise cancellation is active, please make sure to disable it. <br><div>&nbsp;</div>\n\n<div>In this test, you will hear speech in noise saying \"The digits\" followed by <strong>3 digits</strong>. Each digit is a random number between 0 and 9, where 0 is pronounced \"zero.\" Please listen carefully and type the three digits that you hear in the box provided below. If you are uncertain, please write your best guess about the 3 digits, or if you do not hear all of the 3 digits, write only those that you hear, for example: \"0\" or \"01\" or \"012\".</div>",
        "QuestionText_Unsafe": "<h1>&nbsp;</h1>\n\n<h1><b>Hearing Test</b></h1>\n\n<div>&nbsp;</div>\nPlease note that <strong>this is not a medical test</strong> but a quick method for us to check your acoustic environment, attention, hearing, and noise sensitivity. If you are worried about your hearing please consult a qualified doctor.&nbsp;\n\n<br><br>Please use headphones throughout the entire task, and make sure you are in a quiet environment. If your headphones' automatic noise cancellation is active, please make sure to disable it. <br><div>&nbsp;</div>\n\n<div>In this test, you will hear speech in noise saying \"The digits\" followed by <strong>3 digits</strong>. Each digit is a random number between 0 and 9, where 0 is pronounced \"zero.\" Please listen carefully and type the three digits that you hear in the box provided below. If you are uncertain, please write your best guess about the 3 digits, or if you do not hear all of the 3 digits, write only those that you hear, for example: \"0\" or \"01\" or \"012\".</div>",
        "QuestionType": "Matrix",
        "Randomization": {
            "Advanced": None,
            "ConsistentScaleReversal": True,
            "EvenPresentation": False,
            "TotalRandSubset": "",
            "Type": "All"
        },
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
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/1",
                                "Description": "<span class=\"ConjDesc\">If</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/1",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "1": {
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/2",
                                "Conjuction": "And",
                                "Description": "<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/2",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "2": {
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/3",
                                "Conjuction": "And",
                                "Description": "<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/3",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "3": {
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/4",
                                "Conjuction": "And",
                                "Description": "<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/4",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "4": {
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/5",
                                "Conjuction": "And",
                                "Description": "<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/5",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "5": {
                                "ChoiceLocator": "q://QID1213622116/ChoiceTextEntryValue/4/6",
                                "Conjuction": "And",
                                "Description": "<span class=\"ConjDesc\">And</span> <span class=\"QuestionDesc\">&nbsp; Listening Test &nbsp; Please note that this is not a medical test but a quick method for us to contr...</span> <span class=\"LeftOpDesc\">Text Response</span> <span class=\"OpDesc\">Matches Regex</span> <span class=\"RightOpDesc\"> ^\\d{1,3}$ </span>",
                                "LeftOperand": "q://QID1213622116/ChoiceTextEntryValue/4/6",
                                "LogicType": "Question",
                                "Operator": "MatchesRegex",
                                "QuestionID": "QID1213622116",
                                "QuestionIDFromLocator": "QID1213622116",
                                "QuestionIsInLoop": "no",
                                "RightOperand": "^\\d{1,3}$",
                                "Type": "Expression"
                            },
                            "Type": "If"
                        },
                        "Type": "BooleanExpression"
                    },
                    "Message": {
                        "description": "Error Text",
                        "libraryID": "UR_8ldtlrFg8W5ziES",
                        "messageID": "MS_d0c1t8cHvIjvxQi",
                        "subMessageID": "VE_ERROR"
                    }
                }
            }
        },
        "DataExportTag": "Q18",
        "QuestionID": "QID1213622116"
    }
}

FLOW_BLOCK_TEMPLATE = {
    "Type": "BlockRandomizer",
    "FlowID": "FL_28",
    "SubSet": 1,
    "EvenPresentation": True,
    "Flow": [],
}
