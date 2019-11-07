# - * - Coding : utf-8 - * -
import os
import requests
import json
import time

url = 'localhost'
port = '8080'

keys = requests.get('http://'+url+':'+port+'/using/')
keys = keys.json()
print(len(keys))






		

		


