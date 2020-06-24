function sendQuestion() {
            const questionText = $("#user-text")[0].value;
            if (questionText) {
                $("#discussion").prepend('<div class="row">' +
                    '            <div class="col-6"></div>' +
                    '            <div class="question col-6 text-right rounded-pill">' +
                    '                <p class="question"></p>' +
                    '            </div>' +
                    '        </div>' +
                    '<br/>');
                $("#discussion p.question")[0].innerText = questionText

                setTimeout(function() { insertAnswer(questionText); }, 500);
            }
        }

        function insertAnswer(questionText) {
            const answerText = "Voici la réponse : " + questionText;
            $("#discussion").prepend('        <div class="row">' +
                '            <div class="answer col-6 text-left rounded-pill">' +
                '                <p class="answer"></p>' +
                '            </div>' +
                '            <div class="col-6"></div>' +
                '        </div>' +
                        '<br/>');
            $("#discussion p.answer")[0].innerText = answerText
        }