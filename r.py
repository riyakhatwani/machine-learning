import socket
import pyttsx

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("127.0.0.1",8888))
while True:
 eng=pyttsx.init()
 data=(x.recvfrom(1000))
 print data[0]
 eng.say(data[0])
 eng.runAndWait()
 reply=raw_input("plz reply")
 x.sendto(reply,data[1])
 
