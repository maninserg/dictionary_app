from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from PyDictionary import PyDictionary


app = Flask(__name__)
bootstrap = Bootstrap(app)
dictionary = PyDictionary


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
