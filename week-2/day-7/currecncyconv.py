# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:38:22 2019

@author: mv gupta
"""

import requests

url1 = "https://free.currconv.com/api/v7/convert"
url2 = "?q=USD_INR&compact=ultra"
url3 = "&apiKey=f4cda8a8a702b6a09fb6"

url = url1 + url2 + url3
response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
jsondata = response.json()
print(jsondata['USD_INR'])
