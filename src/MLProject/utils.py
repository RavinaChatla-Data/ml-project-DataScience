import os
import sys
from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    print("Reading SQl database started")  ##Logging.info

    try:
        mydb = pymysql.connect(
        host = host,
        user = user,
        password = password,
        db = db
        )
        logging.info(f"Connection Established: {mydb}")   ##changed by gemini
        df = pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        return df
    
    except Exception as ex:
        raise CustomException(ex)
    
