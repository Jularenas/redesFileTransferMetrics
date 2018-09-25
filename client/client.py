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
filehash=0
with open('received_file.txt', 'wb') as f:
    print(s.recv(1024))
    msg="Ready to recieve"
    s.send(msg.encode('utf-8'))
    print ('file opened')
    hashing=s.recv(1024).decode('utf-8')
    print('el hashing es'+hashing)
    while True:
        print('receiving data..	.')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        if(data.decode('utf-8')=='Thank you for connecting'):
            print(done)
        else:			
            f.write(data)

f.close()

with open('received_file.txt','rb') as afile:
        buf=afile.read()
        hasher.update(buf)
hashval=hasher.hexdigest()
print(str(hashval).strip())
print(str(hashing).strip())
if str(hashval).strip()==str(hashing).strip():
    print('Successfully get the file')
    msg='Status:OK'
    s.send(msg.encode('utf-8'))
else:
    print('hash error file not complete')
    msg='Status: File Not Complete'
    s.send(msg.encode('utf-8'))	
s.close()
print('connection closed')