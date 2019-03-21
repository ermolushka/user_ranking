import sqlite3

"""
Create db for saving uploaded file names 
"""
conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('CREATE TABLE people (file_name TEXT)')
print("created")
conn.close()
