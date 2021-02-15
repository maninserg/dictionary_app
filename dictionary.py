from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap
from PyDictionary import PyDictionary


app = Flask(__name__)
bootstrap = Bootstrap(app)
dictionary = PyDictionary()


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if len(request.form["word"]) > 0:
            word1 = request.form["word"]
            return redirect(url_for("find", word=word1), 301)
    return render_template("index.html")


@app.route("/find/", methods=["POST", "GET"])
def find():
    word = request.args.get("word")
    whatis_word = dictionary.meaning(word)
    synonym_word = dictionary.synonym(word)
    antonym_word = dictionary.antonym(word)
    return render_template("find.html", whatis_word=whatis_word,
                           antonym_word=antonym_word,
                           synonym_word=synonym_word,
                           cur_word=word)


if __name__ == "__main__":
    app.run(port=5000, debug=False)
