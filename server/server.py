import socket 	                  								  # Import socket module
import hashlib


port = 8080                    								  # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostname()     								  # Get local machine name
s.bind((host, port))            								  # Bind to the port
s.listen(5)                     								  # Now wait for client connection.

print ('Server listening....')
filename='mytext.txt'
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    msg='Hello Client'
    conn.send(msg.encode('utf-8'))
    data=conn.recv(1024)
    print('Server received',repr(data))
    hasher=hashlib.md5()
    with open(filename,'rb') as afile:
        buf=afile.read()
        hasher.update(buf)
    hashval=hasher.hexdigest()+'\r\n'
    conn.send(hashval.encode('utf-8'))
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
    print('Done sending')
    #msg='Thank you for connecting'
    #conn.send(msg.encode('utf-8'))
    conn.close()