from flask import Flask, render_template
from datetime import date, datetime
import random
import pytz


def process():
    # convert utc server time to aus date
    utcnow = datetime.utcnow().replace(tzinfo=pytz.utc)
    austime = utcnow.astimezone(pytz.timezone("Australia/NSW"))
    date_today = austime.date()

    # seed rng based on date
    seed_val = date_today.toordinal()
    random.seed(seed_val)

    # shuffle names
    names = ["Nico", "Rui", "Kathleen", "Dave", "Manpreet", "Michael"]
    random.shuffle(names)

    display_date = date_today.strftime("%A, %d %B %Y")

    return (names, display_date)


app = Flask(__name__)

@app.route("/")
def hello():
    names, display_date = process()
    return render_template("hello.html", names=names, disp_date=display_date)
