#!/usr/bin/env python
import re, json
from bottle import request, response, route
from predictor import randomforest
from predictor import decisiontrees
from predictor import lstm_mid_onetoone
from predictor import lstm_mid_onetomany
import numpy as np
from sklearn.externals import joblib

@route ('/downthrpt', method='POST')
def downthrpt():	
     response.content_type = 'application/json'
     features = request.json['features']
     model = request.json['model']
     if(model == 'rf'):
        prediction = randomforest(features = np.array(features).reshape(1,1))
     elif(model == 'dt'):
        prediction = decisiontrees(features = np.array(features).reshape(1,1))
     elif(model == 'lstm_onetoone'):
        prediction = lstm_mid_onetoone(features = np.array(features).reshape(1,1))
     elif(model == 'lstm_onetomany'):
        #prediction = lstm_mid_onetomany(features = np.array(features).reshape(1,1))
        prediction = lstm_mid_onetoone(features = np.array(features).reshape(1,1))
        prediction = np.append(prediction,[300.5,300.5,300.5,300.5])
     return json.dumps(prediction.tolist())
