#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#http://data.pr4e.org/intro-short.txt
import socket    #importing socket library

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #creates a socket connection
mysock.connect(('data.pr4e.org',80))        #establish a connection with a domain (data.pr4e.org)  and port (80 - port code for HTTP web server)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #creating a GET request(to be sent to the server) following the HTTP protocol and encoding it in bytes object
mysock.send(cmd) #sending the request through mysock handle

while True:        # printing the retrived data
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()    # closing the connection