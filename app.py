from flask import Flask, render_template
from datetime import date, datetime
import random
import pytz
# from ipdb import set_trace


def get_names_today(date_today: date) -> list:
    """Returns a list of names conditional on whos is rostered for the day"""

    names = ["Nico", "Rui", "Kathleen", "Dave"]

    # add intern-specific work days
    # if date_today.weekday() in (3, 4):
    #     names.append("Manpreet")

    return names


def process():
    # convert utc server time to aus date
    utcnow = datetime.utcnow().replace(tzinfo=pytz.utc)
    austime = utcnow.astimezone(pytz.timezone("Australia/NSW"))
    date_today = austime.date()

    # seed rng based on date
    seed_val = date_today.toordinal()
    random.seed(seed_val)

    # shuffle names, add manpreet if on a Thurs or Fri
    names = get_names_today(date_today)
    random.shuffle(names)

    display_date = date_today.strftime("%A, %d %B %Y")

    return (names, display_date)


app = Flask(__name__)

@app.route("/")
def hello():
    names, display_date = process()
    return render_template("hello.html", names=names, n_names=len(names), disp_date=display_date)
