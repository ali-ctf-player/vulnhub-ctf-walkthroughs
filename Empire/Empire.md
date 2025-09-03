

# Empire Walkthrough

**VulnHub Link:** [Empire](https://www.vulnhub.com/entry/empire-breakout,751/)
**Difficulty:** Easy
**Release Date:** 21 Oct 2021


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

cyber user found 

in 192.168.100.99:80  page source , encoding captured and decoded 

in 192.168.100.99:20000 logged in and executed python reverse shell command

logged as cyber user and user flag captured


## 3.Privilege Escalation

```bash
./tar -cf root.tar /root/
./tar -xvf root.tar
```
and root flag captured.!

