# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:11:06 2019

@author: mv gupta
"""

import json
import requests

Host = "http://13.127.155.43/api_v0.1/sending"

data = {"Phone Number":"9079572643","Name":"Alok","collage name":"PIET","BRANCH":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}


def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/receiving")
    jsondata = response.json()
    return jsondata

print (get_method())