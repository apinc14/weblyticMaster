import pymysql
from flask import Flask, render_template

def initDB():

    print("very start save")
    host = 'localhost'
    port = 3306
    user = 'root'
    password = 'snook1sm00sh0Osmoozh'
    db_name = 'weblyticsDB'

    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db_name,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

def getFromDbTotals():
    return TryTaskSQLQueries('SELECT * FROM totals ORDER BY score DESC LIMIT 20;')
        

def getFromDbPosts():
   return TryTaskSQLQueries('SELECT * FROM posts ORDER BY post_score DESC LIMIT 20;')
  
        
def TryTaskSQLQueries(SqlQuery):
    connection = initDB()
    try:
        # Create a cursor object to interact with the database
        with connection.cursor() as cursor:
            # Define your SQL query to retrieve data from a table
            sql_query_posts = SqlQuery

            # Execute the SQL query
            cursor.execute(sql_query_posts)
            results = cursor.fetchall()

            
            # Fetch all the results as a list of tuples
           

            # Process the retrieved data (replace this with your actual data processing logic)
            for row in results:
                print(row)  # You can replace this with your desired data processing code
           
            connection.close()
            return results

    finally:
        pass
        # Close the database connection when done