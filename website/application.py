from flask import Flask, render_template
import json
from backend import answer_fetcher

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/askpapy')
def askpapy():
    af = answer_fetcher.AnswerFetcher()
    answer = af.find_answer("openclassrooms")
    if answer:
        return json.dumps({"answer": answer.wiki_text, "wiki_url": answer.wiki_url, "map": answer.map})


if __name__ == "__main__":
    app.run(debug=True)
