# Data Transformation Excercise - PYTHON

## How to submit your code assignment

1. Fork the project from GitHub.
2. Make your forked project to **private** 
3. Add **ibmq2c** as member via **Manage Access**. From 'Settings' tab -> 'Manage access' -> 'Invite teams or people' -> Search for **ibmq2c** -> add  **ibmq2c** to this repository.
4. Complete your code and documentation in the forked project.
5. Create a new plain text file in the root folder of the forked project. And make the file name in the format of "your full name", e.g. **Mark Leon**.
6. Notify the code assignment is done or you can contact your employer to notify the same (we would be regularly checking the repo for any checkins).

OR

1. Send the file/s to the interviewer or recruiter and you may ask them to share the file to the concerned point of contact/hiring team. 


<h1>Result Kernel</h1>
<h3>Kernel Results</h3>
![image](https://user-images.githubusercontent.com/41942751/178558429-8bbb016f-e763-4fb5-b40a-5dddb3a895b9.png)
<img src="https://user-images.githubusercontent.com/41942751/178558429-8bbb016f-e763-4fb5-b40a-5dddb3a895b9.png"  width=400 height=400>
<h3>File Results</h3>
![image](https://user-images.githubusercontent.com/41942751/178558667-d256a734-c272-44e2-98ec-60a9874f41aa.png)
<img src="https://user-images.githubusercontent.com/41942751/178558667-d256a734-c272-44e2-98ec-60a9874f41aa.png"  width=400 height=400>

<h1>Code Simply  using some basic methods</h1>
Pandas ---> to convert it to csv file 
time--> to get random substring file name
psycopg2--> connect with database 


## Sources

https://www.tutorialspoint.com/python_data_access/python_postgresql_database_connection.htm#:~:text=To%20establish%20connection%20with%20the,is%20established%20with%20PostgreSQL%20database.

https://www.postgresqltutorial.com/postgresql-python/connect/

# mainlogic
 ## loading data
 

tbname="loan_data"
cursor.execute("select* from loan_data")
#better method
colnames = [desc[0] for desc in cursor.description]
print(colnames)

data = cursor.fetchall();
print("clumnnames: ",len(data))
conn.close()

 ## formating data
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
    
    #adding as columns in f object
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


## creating object for pandas or csv
dataobj={}
for i in range(0,len(f)):
    dataobj[colnames[i]]=f[i]


    
def cop(fname,datab):
    # intialise data of lists
    data =datab
   
         #end check
    print("done",end="/n")
## Create DataFrame
    df = pd.DataFrame(data)
    
    df.to_csv(fname+".csv", mode='a', header=False)


## finally calling 
cop("IBM"+str(time.time())[-4:-1],dataobj)   
print("done")   



