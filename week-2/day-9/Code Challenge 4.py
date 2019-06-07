from bs4 import BeautifulSoup
import requests
import os
import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'employee.db' )


# creating cursor
c = conn.cursor()
#import urllib
c.execute ("""CREATE TABLE employee11(
          pos INTEGER,
          team  TEXT,
          matches INTEGER,
          pOINTS INTEGER,
          Rating INTEGER
          )""")



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
      
col_data = list(zip(A,B,C,D,E))
for item in col_data:
   c.execute("INSERT INTO employee11 VALUES (?,?,?,?,?)", (item))
   
c.execute("SELECT * FROM employee11")

df1 = DataFrame(c.fetchall()) 
df1.columns = ["Position","Team","Weighted matches","Points","Rating"]
conn.commit()
conn.close()
