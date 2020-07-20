# Create a New Python File and Import the Flask Dependency
import datetime as dt
import numpy as np
import pandas as pd

# Dependencies needed for SQLAlchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Create database engine (access to SQLite) for the Flask application much like climate_analysis.ipynb
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect db into our classes
Base = automap_base()
# Reflect our tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a sesison link
session = Session(engine)

# -------- Set Up Flask --------a
# Create a New Flask App Instance (Create a Flask app)
app = Flask(__name__)

# Create a Flask route
@app.route('/')
# forward slash: denote we want to put our data at the root of our routes. 
# Starting point is called root 
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Run a Flask App
# 1) use the command line to navigate to the folder where we’ve saved our code
    #export FLASK_APP=app.py on terminal
    # flask run on the terminal
# http://127.0.0.1:5000/

# Next Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
	filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)
# http://127.0.0.1:5000/api/v1.0/precipitation to see the results

# Station route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results)) # unraveling results into a one-dimensional array
    return jsonify(stations=stations)
# http://127.0.0.1:5000/api/v1.0/stations

# Montly Temperature Route
@app.route("/api/v1.0/tobs")
def temp_monthly():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   results = session.query(Measurement.tobs).\
       filter(Measurement.station == 'USC00519281').\
           filter(Measurement.date >= prev_year).all()
   temps = list(np.ravel(results))
   return jsonify(temps=temps) #As we did earlier, we want to jsonify our temps list, and then return it.
# http://127.0.0.1:5000/api/v1.0/tobs

# Statistics Route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]           

    if not end: 
        results = session.query(*sel).\
           filter(Measurement.date <= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
 # http://127.0.0.1:5000/api/v1.0/temp/2017-06-01/2017-06-30