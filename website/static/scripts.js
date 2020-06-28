function keepScrolling() {
    const doc_body = document.getElementsByTagName("body")
    window.scrollTo(0, doc_body.height);
}

function sendQuestion() {
    const questionText = document.getElementById("user-text").value;

    if (questionText) {
        const discussion = document.getElementsByClassName("discussion-zone")[0];
        discussion.innerHTML += '<div class="row"><div class="col-6"></div><div class="question col-6 text-right"><p class="question-text"></p></div></div><br/>';
        const questions = discussion.getElementsByClassName("question-text");
        questions[questions.length - 1].innerText = questionText;
        keepScrolling();
        fetch("http://127.0.0.1:5000/askpapy")
            .then(function (value) {console.log(value); return value.json()})
            .then(function (data) {insertAnswer(data.answer, data.wiki_url, data.map_url)})
            }
}

function insertAnswer(answerText, wikiUrl, googleMap) {
    const discussion = document.getElementsByClassName("discussion-zone")[0];
    discussion.innerHTML += '<div class="row"><div class="answer col-6 text-left"><p class="answer"></p><p>Si tu veux en savoir plus, clique <a class="wiki">ici</a></p><img class ="img" /></div></div><br/>';
    const answers = discussion.getElementsByClassName("answer");
    const anchors = discussion.getElementsByClassName("wiki");
    const images = discussion.getElementsByClassName("img");
    answers[answers.length-1].innerText = answerText;
    anchors[anchors.length-1].href = wikiUrl;
    images[images.length-1].src = googleMap;
    keepScrolling();
}
    const go_button = document.getElementById("btn")
    go_button.addEventListener("click", sendQuestion)
