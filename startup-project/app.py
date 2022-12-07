
from flask import Flask, request, render_template
import math
import pickle
import sklearn
from sklearn.ensemble import GradientBoostingClassifier
import joblib

model = pickle.load(open("finalized_model.sav", "rb"))


app = Flask(__name__)

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
    proba = predict[0][1]

    return render_template('form.html', success=proba)

if __name__ == "__main__":
    app.run()


