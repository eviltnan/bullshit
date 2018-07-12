from bullshit import horoscope
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_horoscope():
    return render_template("horoscope.html", horoscope=horoscope.generate())


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
