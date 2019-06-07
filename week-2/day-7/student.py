# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:44:55 2019

@author: mv gupta
"""

import json
json_string = """
{
    "faculty 1": {
        "First Name": "Alok",
        "Last Name":"Gupta",
        "Photo":"https://images.pexels.com/photos/257360/pexels-photo-257360.jpeg?cs=srgb&dl=bench-carved-stones-cemetery-257360.jpg&fm=jpg",
        "Department":"Computer",
        "Research Areas":"ML",
        "Contact Details":{
        "Phone No":9079572643,
        "Email":mdgupta.md.1122@gmail.com"
        }
    },
    "faculty 2": {
        "First Name": "Mohit",
        "Last Name":"Kumar",
        "Photo":"https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwje-Yrgo5riAhVJMI8KHd4PAKkQjRx6BAgBEAU&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fnatural%2F&psig=AOvVaw08HUMU-eRCv_EHMtC1fjp4&ust=1557897544887996",
        "Department":"Civil",
        "Research Areas":"DL",
        "Contact Details":{
        "Phone No":9829643733,
        "Email":magupta.mad.1122@gmail.com"
        }
    }
}"""
        
print(json_string)