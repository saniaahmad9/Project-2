import os

import pandas as pd
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine('postgresql://postgres:Chemonics2016@localhost/ISS')
connection = engine.connect()
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table
ISS_Locations = Base.classes.locations
@app.route("/")
def index():
   """Return the homepage."""
   return render_template("index.html")
@app.route("/cities")
def cities():
   """Return a list of cities."""
   # Use Pandas to perform the sql query
   locations = pd.read_sql('select * from locations', connection)
   # Return a list of the column names (sample names)
   return jsonify(locations)
if __name__ == "__main__":
   app.run()
