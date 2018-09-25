# client.py
import hashlib
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 8080                    # Reserve a port for your service.

s.connect((host, port))
msg="Hello server!"
s.send(msg.encode('utf-8'))
hasher=hashlib.md5()
with open('received_file.txt', 'wb') as f:
    print ('file opened')
    i=0
    while True:
        print('receiving data..	.')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        if(data=='valor del hash'):
            print('hashing')
        else:
            f.write(data)

f.close()

print('Successfully get the file')
s.close()
print('connection closed')