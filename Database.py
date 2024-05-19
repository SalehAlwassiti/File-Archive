import sqlite3
import hashlib

username_tupil = []

def registeration(inputed_username, inputed_password, inputed_ID, inputed_level):
    Database = sqlite3.connect('Users.db')
    cur = Database.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS UsersPasses(username,password,ID,level)")

    username = inputed_username
    password = hashlib.sha256(inputed_password.encode()).hexdigest()
    Id = inputed_ID
    level = inputed_level
    values = [username,password,Id,level]
    cur.execute("INSERT INTO UsersPasses VALUES(?,?,?,?)",values)
    
    Database.commit()
