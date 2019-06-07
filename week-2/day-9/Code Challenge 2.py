"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.4
"""

import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://Madhuvrat_056:alokgupta@cluster0-shard-00-00-qsyps.mongodb.net:27017,cluster0-shard-00-01-qsyps.mongodb.net:27017,cluster0-shard-00-02-qsyps.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb = client.db_University

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.student.insert_one(
            {
            "Student_Name" : idd,
            "Student_Age" : first,
            "Student_Roll_no" : last,
            "Student_Branch" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.student.find()
    for i in user:
        print (i)




add_employee('Sylvester',25,18,'50000')
add_employee('Sylvester1',26,18,'500000')
add_employee('Sylvester2',27,18,'5000000')
add_employee('Sylvester3',28,18,'50000000')
add_employee('Sylvester4',29,18,'500000000')
add_employee('Sylvester5',30,18,'50000000')
add_employee('Sylvester6',31,18,'50000000')
add_employee('Sylvester7',32,18,'50000000')

fetch_all_employee()


