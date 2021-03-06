#!/usr/bin/env python
# encoding: utf-8

import requests 
import re, json

'''
O parâmetro features é a vazão do tempo corrente (t) em KB/s 
O parâmetro model é o modelo de predição
O serviço retorna uma lista com 5 valores de vazão em KB/s dos tempos t+1,...,t+5
'''

url     = "http://10.208.200.250:8000/downthrpt"
data    = {'features': [100.738386],'model': 'lstm_onetomany'}   #features: vazão em KB/s; model: modelo de predição
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r       = requests.post(url, data=json.dumps(data), headers=headers)
print r.text
