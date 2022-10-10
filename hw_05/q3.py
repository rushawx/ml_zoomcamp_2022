# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:46:00 2022

@author: rusha
"""

import pickle


def predict_single(customer, dv, model):
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[:,1]
    return y_pred[0]


with open('dv.bin', 'rb') as dv_in:
    dv = pickle.load(dv_in)

with open('model1.bin', 'rb') as model_in:
    model = pickle.load(model_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

print(round(predict_single(client, dv, model), 3))
