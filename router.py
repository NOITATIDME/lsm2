from flask import Flask
from flask.templating import render_template
import movie_api as ma
import weather_api as we

app = Flask(__name__)


@app.route("/")
def index():
    # flask는 template안에 있으면 무조건 해석해준다. # render_template 입력시 자동으로 import된다.
    return render_template("index.html", movies=ma.CallMovieApi(), weatherDict=we.CallWeatherApi())


if __name__ == "__main__":
    app.run(debug=True)
