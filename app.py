from flask import Flask, render_template
from datetime import date, datetime
import random
import pytz

# convert utc server time to aus date
utcnow = datetime.utcnow().replace(tzinfo=pytz.utc)
austime = utcnow.astimezone(pytz.timezone("Australia/NSW"))
date_today = austime.date()

# seed rng based on date
seed_val = date_today.toordinal()
random.seed(seed_val)

# shuffle names
names = ["Nico", "Rui", "Kathleen", "Dave"]
random.shuffle(names)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", names=names, date_today=date_today)
