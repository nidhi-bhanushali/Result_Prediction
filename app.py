from flask import Flask, request,jsonify,render_template
import numpy as np
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # int_features = {x for x in request.form.values()}
    # final_features = [np.array(int_features)]
    sex = request.form.get("gender")
    final_features = [sex]

    age = request.form.get("age")
    final_features.append(age)

    famsize = request.form.get("famSize")
    final_features.append(famsize)

    pStatus = request.form.get("pcs")
    final_features.append(pStatus)

    mEdu = request.form.get("mEdu")
    final_features.append(mEdu)

    fEdu = request.form.get("fEdu")
    final_features.append(fEdu)

    mJob = request.form.get("mJob")
    final_features.append(mJob)

    fJob = request.form.get("fJob")
    final_features.append(fJob)

    travelTime = request.form.get("travelTime")
    final_features.append(travelTime)

    studyTime = request.form.get("studyTime")
    final_features.append(studyTime)

    failures = request.form.get("failures")
    final_features.append(failures)

    famSup = request.form.get("famSup")
    final_features.append(famSup)

    paid = request.form.get("paid")
    final_features.append(paid)

    activites = request.form.get("activites")
    final_features.append(activites)

    higherStudies = request.form.get("higherStudies")
    final_features.append(higherStudies)

    internet = request.form.get("internet")
    final_features.append(internet)

    romantic = request.form.get("romantic")
    final_features.append(romantic)

    famRel = request.form.get("famRel")
    final_features.append(famRel)

    freeTime = request.form.get("freeTime")
    final_features.append(freeTime)

    goOut = request.form.get("goOut")
    final_features.append(goOut)

    dalc = request.form.get("dalc")
    final_features.append(dalc)

    walc = request.form.get("walc")
    final_features.append(walc)

    health = request.form.get("health")
    final_features.append(health)
    
    absences = request.form.get("absences")
    final_features.append(absences)

    g1 = request.form.get("g1")
    if g1 != None:
        print(g1)
        final_features.append(g1)

    g2 = request.form.get("g2")
    if g2 != None:
        print(g2)
        final_features.append(g2)

    int_features = [int(x) for x in final_features]
    final_features = np.array(int_features).reshape(1, -1)
    print(final_features)

    if(g1 != None and g2 != None):
        model = pickle.load(open('modelG1G2.pkl', 'rb'))
        print(model)
    elif(g2 == None):
        model = pickle.load(open('modelG1.pkl', 'rb'))
        print(model)
        print('g1')
    else:
        model = pickle.load(open('modelN.pkl', 'rb'))
        print(model)
        print('none')

    # final_features = final_features.reshape(-1 , 1)
    prediction = model.predict(final_features)
   
    output = round(prediction[0], 2)
    if(output == 0):
        prediction_text = 'The student needs assitance'
    else:
        prediction_text = 'The student is doing well'
    print(output)

    return render_template('index.html', prediction_text= prediction_text)

if __name__ == '__main__':
    app.run()
