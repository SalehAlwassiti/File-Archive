import sqlite3
import socket
import threading
import hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)

def connection_handling(client):
    
    client.send('Username? '.encode())
    username = client.recv(1024).decode()
    client.send('Password? '.encode())
    password = client.recv(1024)
    
    hashed_password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect('Users.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM UsersPasses WHERE username = ? AND password = ?", (username,hashed_password))

    Gotten = cur.fetchall()

    if Gotten:
        user_level = Gotten[-1]
        user_level = user_level[-1]
        sending = 'successful'
    else:
        sending = 'failed'
        user_level = 'null'

    client.send(user_level.encode())
    client.send(sending.encode())

while True:
    cm , address = server.accept()
    threading.Thread(target = connection_handling, args=(cm,)).start()
