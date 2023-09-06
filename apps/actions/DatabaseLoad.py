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

def getFromDb():
    connection = initDB()
    try:
        # Create a cursor object to interact with the database
        with connection.cursor() as cursor:
            # Define your SQL query to retrieve data from a table
            sql_query_posts = '''SELECT *
                                FROM posts
                                ORDER BY post_score DESC
                                LIMIT 20;'''

            sql_query_totals = 'SELECT * FROM totals ORDER BY score DESC LIMIT 20;'

            

            # Execute the SQL query
            cursor.execute(sql_query_posts)
            resultsPosts = cursor.fetchall()

            cursor.execute(sql_query_totals)
            resultsTotals = cursor.fetchall()
            # Fetch all the results as a list of tuples
           

            # Process the retrieved data (replace this with your actual data processing logic)
            for row in resultsPosts:
                print(row)  # You can replace this with your desired data processing code
            for row in resultsTotals:
                print(row)  # You can replace this with your desired data processing code
            connection.close()
            return resultsPosts, resultsTotals

    finally:
        pass
        # Close the database connection when done
        
