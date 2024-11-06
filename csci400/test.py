import MySQLdb

try:
    # Establish the connection
    conn = MySQLdb.connect(
        host="34.125.69.91",          # Database host
        user="t1",                    # Database username
        passwd="YWQQEg1QwgVTc40K",    # Database password
        db="f24_housing_db",          # Database name
        ssl={}                         # Disable SSL by passing an empty dictionary
    )
    print("Connection successful!")
    
    # Create a cursor and execute a test query
    cursor = conn.cursor()
    cursor.execute("SELECT VERSION();")
    version = cursor.fetchone()
    print("Database version:", version)

except MySQLdb.Error as e:
    print("Error connecting to database:", e)

finally:
    # Close the connection
    if conn:
        conn.close()