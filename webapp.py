import os

from flask import Flask, render_template

from bullshit import horoscope

app = Flask(__name__)


@app.route("/")
def get_horoscope():
    return render_template("horoscope.html", horoscope=horoscope.generate())


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=os.environ.get("PORT", 80))
