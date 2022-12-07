

# Import Flask to build web app
from flask import Flask, render_template, redirect, url_for,jsonify, request
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, MetaData, Table
from config import db_password
import pandas as pd
import psycopg2
import json
import pickle

model = pickle.load(open("model.pkl", "rb"))

# Setup Flask
app = Flask(__name__)

# Set path to the database
db_string = f"postgresql://postgres:{db_password}@startup-db.c60crnyd8gs4.us-east-1.rds.amazonaws.com"

# Create enginge to connect with db
engine = create_engine(db_string)

# Create inspector to inspect db
inspector = inspect(engine)

# Get the db as a df and save it as a json file
startup_df = pd.read_sql_table('startup_alldata',db_string)
startup_df.to_json('startup.json')

@app.route("/")
def initial():
    return render_template("index.html")


### Define our about page 
@app.route("/model")
def model():

    return render_template("model.html")


print(startup_df)



if __name__ == "__main__":
    app.run(debug=True)