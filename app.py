# import pandas as pd
from flask import Flask, jsonify, request
import pickle

# load model
model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])
def predict():
    
    # predictions
    result = model.predict([[request.form['q1'],request.form['q2'],request.form['q3'],request.form['q4'],request.form['q5'],request.form['q6'],request.form['q7'],request.form['q8'],request.form['q9'],request.form['q10']]])

    # send back to browser
    output = {'prediction': result[0]}

    # return data
    return jsonify(results=output)
    # return 'hi'

if __name__ == '__main__':
    app.run(port = 5000, debug=True)