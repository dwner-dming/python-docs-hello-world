from flask import Flask, render_template
from datetime import date
import random

# seed rng based on date
seed_val = date.today().toordinal()
random.seed(seed_val)

# shuffle names
names = ["Nico", "Rui", "Kathleen", "Dave", "Michael"]
random.shuffle(names)

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("hello.html", names=names, date_today=date.today())
