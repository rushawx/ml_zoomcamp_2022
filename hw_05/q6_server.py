# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:51:48 2022

@author: rusha
"""

import pickle
from flask import Flask, request, jsonify


def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]


with open('dv.bin', 'rb') as dv_in:
    dv = pickle.load(dv_in)

with open('model2.bin', 'rb') as model_in:
    model = pickle.load(model_in)

app = Flask('default-app')

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    prediction = round(predict_single(client, dv, model), 3)
    
    return jsonify(prediction)

if __name__=='__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)
