import socket 	                  								  # Import socket module
import hashlib
import datetime
import threading
outer_lock = threading.Lock()     
condition = threading.Condition()
n=2																  #Number of clients
id=0															  #IdForThread
ready=0															  #ThreadsReadyToSend
threadList=[]													  #ThreadList
port = 8080                    								  	  # Reserve a port for your service.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)             # Create a socket object
host = socket.gethostname()     								  # Get local machine name
s.bind((host, port))            								  # Bind to the port
s.listen(5)                     								  # Now wait for client connection.

class myThread (threading.Thread):
   def __init__(self, threadID,conn,condition,lock):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.conn = conn
      self.condition = condition
      self.lock = lock
   def run(self):
      conn=self.conn
      data = conn.recv(1024)
      global ready
      global n
      print('Server received', repr(data))
      msg='Hello Client'
      conn.send(msg.encode('utf-8'))
      data=conn.recv(1024)
      with condition:
         ready= ready +1
         if(ready==n):
             self.condition.notifyAll()
         else:
             self.condition.wait()	  
      msg=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      conn.send(msg.encode('utf-8'))
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

print ('Server listening....')
filename='visible.txt'
while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('Got connection from', addr)
    thread = myThread(id,conn,condition,outer_lock)
    id=id+1
    thread.start()
    
    
    
