import socket 
import pyttsx

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
 eng=pyttsx.init()
 msg=raw_input("enter msg to send:")
 x.sendto (msg,("127.0.0.1",8888))
 y=(x.recvfrom(100))
 print y[0]
 eng.say(y[0])
 eng.runAndWait()





