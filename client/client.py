# client.py
import math
import time
import datetime
import hashlib
import os
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = '157.253.202.20'     # Get local machine name
port = 8080                    # Reserve a port for your service.
filename='received_file.txt'
s.connect((host, port))
msg="Hello server!"
s.send(msg.encode('utf-8'))
hasher=hashlib.md5()
filehash=0
timeend=0
timestamp=0
with open(filename, 'wb') as f:
    print(s.recv(1024))
    msg="Ready to recieve"
    s.send(msg.encode('utf-8'))
    print ('file opened')
    timestamp=s.recv(1024)
    print('timeStart'+timestamp.decode('utf-8')+'\n')
    hashing=s.recv(32).decode('utf-8')
    print('el hashing es '+hashing)
    while True:
        print('receiving data..	.')
        data = s.recv(1024)
        if not data:
            break
        # write data to a file
        if(data=='Thank you for connecting'):
            print(done)
        else:			
            f.write(data)

f.close()
timeend=datetime.datetime.now()

with open(filename, 'r') as fin:
    data = fin.read().splitlines(True)
with open(filename, 'w') as fout:
    fout.writelines(data[1:])
with open(filename,'rb') as afile:
        buf=afile.read()
        hasher.update(buf)
hashval=hasher.hexdigest()
status=0
print(str(hashval).strip())
print(str(hashing).strip())
status=0
print(str(hashval).strip()==str(hashing).strip())
timeSent=0

if str(hashval).strip()==str(hashing).strip():
    print('Successfully get the file')
    start=datetime.datetime.strptime(timestamp.decode('utf-8'),"%Y-%m-%d %H:%M:%S")
    print(start)
    print(timeend)
    print((timeend-start).total_seconds())
    timeSent=abs((timeend-start).total_seconds())
    msg='Status:OK'
    status=msg
    s.send(msg.encode('utf-8'))
else:
    print('hash error file not complete')
    msg='Status: File Not Complete'
    status=msg
    s.send(msg.encode('utf-8'))	
s.close()
print('connection closed')



with open('report1_1.txt', 'wb') as f:
    f.write('500.txt \n'.encode('utf-8'))
    f.write((datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'\n').encode('utf-8'))
    f.write((filename+'\n').encode('utf-8'))
    f.write((status+'\n').encode('utf-8'))
    f.write(str(os.path.getsize(filename)).encode('utf-8'))
    f.write((str(timeSent)+'\n').encode('utf-8'))
