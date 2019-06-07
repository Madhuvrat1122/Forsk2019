from bs4 import BeautifulSoup
import requests
#import urllib



#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

right_table=soup.find('table', class_='table')

A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())

import pandas as pd
from collections import OrderedDict

col_name = ["Position","Team","Weighted matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[A,B,C,D,E]))
df = pd.DataFrame(col_data) 
df.to_csv("former1.csv")
