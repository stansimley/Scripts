import pymysql as mdb
import pandas as pd
from sqlalchemy import create_engine
import glob
import os
import subprocess
import chardet

'''google cloud info and folder path'''
instance = e.g. 'stanley-database-test:asia-southeast1:stanley-database-test1'
user = e.g. 'root'
password =
host = '127.0.0.1'
port = '3306'
database =
folder_path =
cloud_sql_proxy_path = ../cloud_sql_proxy

#run cmd command for google cloud sql proxy to use python
subprocess.Popen(cloud_sql_proxy_path + ' -instances={}=tcp:{}'.format(instance, port))

#connect to database
con = mdb.connect(host, user, password, database, local_infile=True)
#create cursor
cursor = con.cursor()
#create sqlalchemy engine for converting Pandas Dataframe to SQL table
engine = create_engine('mysql+pymysql://'+user+':'+password+'@'+host+':'+ port+'/'+database, echo=False)

#get paths of all csv files in folder
all_files = glob.glob(folder_path + "/*.csv")
print("Found {} csv files in folder".format(len(all_files)))

#write each Pandas Dataframe to SQL table iteratively
print("Note: Name of table in database corresponds to name of .csv file. Please use unique names for different tables.")
for file_path in all_files:
    file_name = os.path.basename(file_path).replace('.csv','') #name of csv file
    #to get encoding of file and confidence level- delete next 3 lines if not applicable
    #raw_data = open(file_path, "rb").read() 
    #file_encoding = chardet.detect(raw_data) 
    #print("Creating table for {}, file encoding:{}".format(file_name, file_encoding))
    df = pd.read_csv(file_path) # optional arguments depending on .csv file specifications: sep =';', skiprows=1, encoding=file_encoding.get('encoding')
    df.columns = [''.join(char for char in column.title() if char.isalnum()) for column in df.columns] #change column names to SQL convention
    try:
        df.to_sql(name=file_name, con=engine, index=False) #if_exists = 'replace' or 'append'
    except:
        error = True
        print("[ERROR] File not uploaded. Please check if the table:{} aleady exists".format(file_name))
        continue
if not error:
    print("SUCCESS! Uploaded all files to database")
else:
    print("Uploaded files without error")

print("[Double Check] Querying dataabase for first row in first table:")
first_csv_name = os.path.basename(all_files[0]).replace('.csv','')
query = 'SELECT * FROM {}'.format(first_csv_name)
cursor.execute(query)
print(cursor.fetchone())

con.commit()
print("Changes committed")
con.close()
