"""Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""

import os
import sqlite3
from pandas import DataFrame
conn = sqlite3.connect ('db_University')
c = conn.cursor()
c.execute ("""CREATE TABLE students4(
          Student_Name TEXT,
          Student_Age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("INSERT INTO students4 VALUES ('Sylvester',25,20,'CSE')")
c.execute("SELECT * FROM students4")

print ( c.fetchall() )

# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Name","Age","Roll NO","Branch"]

df.to_csv(df)
# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()
