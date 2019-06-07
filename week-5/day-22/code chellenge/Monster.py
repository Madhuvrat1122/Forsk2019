"""
Code Challenge - 
 This is a pre-crawled dataset, taken as subset of a bigger dataset 
 (more than 4.7 million job listings) that was created by extracting data 
 from Monster.com, a leading job board.
 
 
 
 Remove location from Organization column?
 Remove organization from Location column?
 
 In Location column, instead of city name, zip code is given, deal with it?
 
 Seperate the salary column on hourly and yearly basis and after modification
 salary should not be in range form , handle the ranges with their average
 
 Which organization has highest, lowest, and average salary?
 
 which Sector has how many jobs?
 Which organization has how many jobs
 Which Location has how many jobs?
"""
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('monster_com-job_sample.csv',na_values=[''])
dataset=dataset.iloc[:,[8,9,11,12]]
dataset = dataset[pd.notnull(dataset['location'])]
dataset = dataset[pd.notnull(dataset['organization'])]
dataset.index=range(dataset.shape[0])
#replaing organization from location
def check(item):
    if re.search(r', [A-Z]{2}',item):
        return True
    else:
        return False
for i in range(len(dataset)):
    if check(dataset.iloc[i,1]):
        dataset.iloc[i,0],dataset.iloc[i,1]=dataset.iloc[i,1],dataset.iloc[i,0]      
#remove garbage value from location and organization and sector
not_address=[]
for i in range(len(dataset)):
    if len(dataset.iloc[i,0])>50:
        not_address.append(i)
    if len(dataset.iloc[i,1])>80:
        not_address.append(i)
dataset.drop(labels=not_address,axis=0,inplace=True)
dataset.index=range(dataset.shape[0])
#zip code in location
for item in dataset['location'].index:
    result = ''.join([i for i in dataset['location'][item] if not i.isdigit()])
    dataset['location'][item]=result
#removing blank addresses
not_address=[]
for i in range(len(dataset)):
    if len(dataset.iloc[i,0])==0:
        not_address.append(i)
dataset.drop(labels=not_address,axis=0,inplace=True)
dataset.index=range(dataset.shape[0])
###which Sector has how many jobs?
from collections import Counter
print("Sector :",Counter(dataset.location).most_common())
###Which organization has how many jobs?
print("Organization :",Counter(dataset.organization).most_common())
###Which location has how many jobs?
print("Location :",Counter(dataset.location).most_common())
### Which organization has highest, lowest, and average salary?
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('monster_com-job_sample.csv')
dataset=dataset.iloc[:,[8,9,11,12]]
dataset = dataset[pd.notnull(dataset['location'])]
dataset = dataset[pd.notnull(dataset['organization'])]
dataset = dataset[pd.notnull(dataset['salary'])]
salary=dataset.salary.tolist()
dataset.index=range(dataset.shape[0])
year=[]
month=[]
not_salary=[]
for i in range(len(dataset)):
    try:
        if 'hour' in str(dataset.iloc[i,2]):
            if len(dataset.iloc[i,2].split())<3:
                dataset.iloc[i,2]=float(dataset.iloc[i,2].split()[0].replace(',','').replace('$','').replace('+',''))*9.0*250
            else:
                hour=[]
                hour=dataset.iloc[i,2].split()
                dataset.iloc[i,2]=(float(hour[0].replace(',','').replace('$','').replace('+',''))+float(hour[2].replace(',','').replace('$','').replace('+','')))*9.0*250.0
        elif 'year' in str(dataset.iloc[i,2]):
            if len(dataset.iloc[i,2].split())<3:
                dataset.iloc[i,2]=float(dataset.iloc[i,2].split()[0].replace(',','').replace('$','').replace('+',''))
            else:
                year=[]
                year=dataset.iloc[i,2].split()
                dataset.iloc[i,2]=(float(year[0].replace(',','').replace('$','').replace('+',''))+float(year[2].replace(',','').replace('$','').replace('+','')))
        elif '/month' in str(dataset.iloc[i,2]):
            month=[]
            month=dataset.iloc[i,2].split()
            dataset.iloc[i,2]=(float(month[0].replace(',',''))+float(month[2].replace(',','')))*12.0
        elif 'Up to' in str(dataset.iloc[i,2]):
            dataset.iloc[i,2]=float(dataset.iloc[i,2].split()[2].replace('$',''))
        else:
            not_salary.append(i)
    except:
        not_salary.append(i)
dataset.drop(labels=not_salary,axis=0,inplace=True)
dataset.index=range(dataset.shape[0])
### Which organization has highest, lowest, and average salary?
print("Organization has highest salary :",dataset[dataset.salary==dataset.salary.max()]['organization'])
print("Organization has highest salary :",dataset[dataset.salary==dataset.salary.min()]['organization'])
print("Organization has highest salary :",dataset[dataset.salary>=dataset.salary.mean()].head(1))


        
             

    
       
            
        

            
        

