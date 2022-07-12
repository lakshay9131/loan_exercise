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

## Database Details: postgres
```
Database type : PostgresSQL
host: f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud
port: 30835
dbname: q2c
Username : q2c_user
password : passw0rd
```

## Code assignment instruction
* Create a Python application/file/script(s) (e.g test.py).
* Using Python, create a connection to the postgres database using the database connection details as provided above.
* Load the data from the q2c database (schema name : public | table name : loan_data) and perform the following operation to generate your result:
  * Create a new column called **new term**, for the records with **term** is equal to '36 months' and **loan_status** is not equal to 'Fully Paid' update **new term** coumn with existing value of (**term** + 12 months) 
  * Create a new column called **int_rates_add_2pct**, for every record udpate **int_rates_add_2pct** column with existing value of (**int_rate** + 2%).
* Ouput the result into a csv file and submit the file.
* Please also submit the Python script(s) used in the coding assignment. 
* Create a requirement.txt file with all dependencies used. 

## Optional
In addition to the code assignment instruction above, you may also perform the following as bonus:
 
- Generate a model to predict which entry will have loan_status equals to 'Fully Paid'.
- Please share the notebook(s)/python script(s) that you created to generate the above.
- For each major step involved, please explain the reason why you are implementing the step.

Note : the account q2c_user only have the read access. The operation should be performed on dataframe and output the result to csv file. 
