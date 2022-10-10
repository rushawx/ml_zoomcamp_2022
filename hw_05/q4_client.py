# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:58:24 2022

@author: rusha
"""

import requests

url = 'http://localhost:9696/predict'
customer = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}

response = requests.post(url, json=customer)
result = response.json()

print(result)
