import pandas as pd
from apyori import apriori
dataset = pd.read_csv('BreadBasket_DMS.csv')
#first task
df =  (dataset[dataset['Item']=="NONE"]).index
dataset = dataset.drop(df)
dataset = dataset.reset_index(drop=True)
dataset['Item'].value_counts().head(15).plot.pie()
#second task
list1=[]
dataset.groupby('Transaction')['Item'].apply(lambda x:list1.append(list(set(x))))
from apyori import apriori
rules = apriori(list1, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)
results = list(rules)
for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
#third task
for item in list1:
    items= item[0]
    pair = item[1:] 
    print("Associated_item for {} are {}  ".format(items ,pair))  
