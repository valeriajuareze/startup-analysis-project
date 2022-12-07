
from flask import Flask, request, render_template
import math
from config import db_password
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, MetaData, Table
from config import db_password
import pandas as pd
import psycopg2
import json

import pickle

#### import model 
model = pickle.load(open("finalized_model.sav", "rb"))
### start database string
db_string = f"postgresql://postgres:{db_password}@startup-db.c60crnyd8gs4.us-east-1.rds.amazonaws.com"

# Create enginge to connect with db
engine = create_engine(db_string)
# Create inspector to inspect db
inspector = inspect(engine)
# Get the db as a df and save it as a json file
startup_df = pd.read_sql_table('startup_alldata',db_string)
startup_df.to_json('startup.json')

app = Flask(__name__)

print(startup_df)

@app.route('/')
def succes_calc():
    return render_template('form.html')

@app.route('/calculate_success', methods=['POST'])
def probability_calc():
    print("hello")
    first_funding = float(request.form['first_funding'])
    last_funding = float(request.form['last_funding'])
    first_milestone = float(request.form['first_milestone'])
    last_milestone = float(request.form['last_milestone'])
    state = request.form['state']
    relationship = float(request.form['relationships'])
    rounds = float(request.form['rounds'])
    milestones = float(request.form['milestones'])
    category = request.form['category']
    vc = float(request.form['vc'])
    angel = float(request.form['angel'])
    series_a = float(request.form['seriesa'])
    series_b = float(request.form['seriesb'])
    series_c = float(request.form['seriesc'])
    series_d = float(request.form['seriesd'])
    average_participants = float(request.form['avg_participants'])
    reached_milestone = float(request.form['reached_milestone'])
    founded_funding = float(request.form['founded_funding'])
    first_last_funding = float(request.form['first_last_funding'])
    funding = float(request.form['funding'])
    top500= float(request.form["top500"])
    gdp = float(request.form['gdp'])
    
    for state_name in ["is_ca", "is_ny", "is_ma", "is_tx", "is_otherstate"]:
        if state_name == state:
            globals()[state_name] = 1
        else:
            globals()[state_name] = 0
    
    for category_name in ["is_software", "is_biotech", "is_web", "is_mobile", "is_enterprise", "is_gamesvideo", "is_ecommerce", "is_advertising","is_consulting", "is_other"]:
        if category_name == category:
            globals()[category_name] = 1
        else:
            globals()[category_name] = 0

    ##success = is_enterprise
    list1 = []
    list1.append([gdp,first_funding, last_funding, first_milestone, last_milestone,relationship,rounds, funding, milestones, is_ca, is_ny,
    is_ma, is_tx, is_otherstate, is_software, is_web, is_mobile, is_enterprise, is_advertising, is_gamesvideo, is_ecommerce, is_biotech,is_consulting, is_other, vc, angel, series_a, series_b, series_c, series_d, average_participants,top500, reached_milestone,founded_funding, first_last_funding ])

    predict = model.predict_proba(list1)
    print(predict)
    proba = predict

    return render_template('form.html', success=proba)

if __name__ == "__main__":
    app.run()


