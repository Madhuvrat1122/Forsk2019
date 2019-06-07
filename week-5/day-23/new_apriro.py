import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

#removing nun values
transactions1 = []

for i in range(0, 7501):
    transactions = []
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    for j in range(0, 20):
        if str(dataset.values[i,j]) == 'nan':
            pass
        else:
            transactions.append(str(dataset.values[i,j]))
    transactions1.append(transactions)



# Training Apriori on the dataset

rules = apriori(transactions1, min_support = 0.003, min_confidence = 0.25, min_lift = 4)
#min_support--> greater than 3 per day so,per week = 21 -->min_support=21/7501 =0.3
#min_confidence -->25% 
#min_lift --> for  strong association > 1

# Visualising the results
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
