# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:16:56 2022

@author: ASUS
"""

import psycopg2
import time
import pandas as pd
host ="f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud"
port ="30835"
dbname="q2c"
Username="q2c_user"
password="passw0rd"
#establishing the connection
conn = psycopg2.connect(
   database=dbname, user=Username, password=password, host=host, port= port
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)




#loading data 
tbname="loan_data"
cursor.execute("select* from loan_data")
#better method
colnames = [desc[0] for desc in cursor.description]
print(colnames)

data = cursor.fetchall();
print("clumnnames: ",len(data))
conn.close()



#formatiing data for datacsv columnwise   
tt=0
f=[]
if("new term" not in colnames):
    colnames.append("new term")
if("int_rates_add_2pct" not in colnames):
    colnames.append("int_rates_add_2pct")

for i in colnames:
    i=[i]
    f.append(i)
 
# making list of columns in 2d array
lent=len(colnames)
print(len(f))
for i in data:
    term=i[5]
    i1=[]
    i1=list(i)
    loans=i[11]
    tr=str(float(i[6])+2)
    nterm="None"
    if(loans!="Fully Paid" and term=="36 months"):
        nterm="48 months"
        tt+=1
        #print(tt)
    
    i1.append(nterm)
    #print("S")
    i1.append(tr)
    for j in range(0,lent):
       if(len(f)>j):
          f[j].append(i1[j])
          #print(f)
       else:
         nl=[i1[j]]
         #print(tt)
         f.append(nl)
         #print(f)
    

    #finaldata.append(i1)

print(len(f),end="\n")


#creating object for pandas
dataobj={}
for i in range(0,len(f)):
    dataobj[colnames[i]]=f[i]


    
def cop(fname,datab):
    # intialise data of lists
    data =datab
   
         #end check
    print("done",end="/n")
# Create DataFrame
    df = pd.DataFrame(data)
    
    df.to_csv(fname+".csv", mode='a', header=False)


#finally calling 
cop("IBM"+str(time.time())[-4:-1],dataobj)   
print("done")   
    
    
 
#print(cnamelist[22])
#print(data[2][22])
#i[11], loan status Fully paid




#trial codes
def trial():
 for i in range(0,lent):
    print(i,end=",")
    
 f=[]
 for i in range(0,5):
    if(len(f)>i):
        print("y")
    else:
        nl=[i]
        f.append(nl)
        print(f)
 cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ='loan_data'")
 cnamelist=cursor.fetchall()
 print("clumnnames: ",len(cnamelist))
        
        
        
        
        


        
        
        
  
