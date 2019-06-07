# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:07:22 2019

@author: mv gupta
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=1ac9d63870fb6abf5889007ea8226e2c"

url = url1 + url2 + url3
response = requests.get(url)
jsondata = response.json()
print("latitude :",jsondata['coord']['lat'])
print("longitude :",jsondata['coord']['lon'])
print("wind :",jsondata['wind']['speed'])
print("sunrise :",jsondata['sys']['sunrise'])
print("sunset :",jsondata['sys']['sunset'])