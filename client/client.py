# client.py
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
timeend=datetime.datetime.now()

with open('received_file.txt','rb') as afile:
        buf=afile.read()
        hasher.update(buf)
hashval=hasher.hexdigest()
print(str(hashval).strip())
print(str(hashing).strip())
timeDone=0
status=0
if str(hashval).strip()==str(hashing).strip():
    print('Successfully get the file')
    start=datetime.datetime.strptime(timestamp.decode('utf-8'),"%Y-%m-%d %H:%M:%S")
    print(start)
    print(timeend)
    print((timeend-start).total_seconds())
    timeDone=(timeend-start).total_seconds()
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



with open('report.txt', 'wb') as f:
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").encode('utf-8'))
    f.write('\n')
    f.write(filename.encode('utf-8'))
	f.write('\n')
    f.write(timeDone)
    f.write('\n')
    f.write(status)