import os
from dotenv import load_dotenv
import pymysql
from apps.config import config_dict
from apps import create_app
from flask import Flask


def dbPerform( action, isInboundBool ):
    dbCon, cursor = init_Db()
    try:
        if inboundBool: 
         # Execute the create table queries
         cursor.execute(action)
        else: 
            retrievedInfo = cursor.execute(action)
            print('Database manipulated successfully.')
    except pymysql.connector.Error as err:
              print(f"Error editing {err}")
    finally:
           cursor.close()
           dbCon.close()
           print('succ')
    if not inboundBool: 
         return retrievedInfo
def dbActionInsertUser( name, password, email, billingDate, isPremium ):
    insertData = """ 
            INSERT INTO Customers (username, password, email, billingDate, activePremium,);
            VALUES ('{}','{}','{}','{}','{}');
    """.format( name, password, email, billingDate, isPremium )
    return insertData
def dbActionRetreiveUser( name, password, billingDate, isPremium ):
    data = """ 
            SELECT  FROM users 
            VALUES ('{}','{}','{}','{}');
    """.format( name, password, billingDate, isPremium )
    return data
def dbActionReturnNews():
    returnNews = """
    SELECT * WHERE {};
    """.format()
    print('return')
    return create_table_query
   