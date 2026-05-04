import sqlite3

def get_user_data(user_input_id):
    # This is a CRITICAL vulnerability
    # We are concatenating user input directly into the SQL query
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    
    query = "SELECT * FROM users WHERE id = " + user_input_id 
    
    print(f"DEBUG: Executing query: {query}")
    cursor.execute(query)
    return cursor.fetchall()
    #comment
