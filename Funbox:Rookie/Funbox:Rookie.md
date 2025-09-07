

# Funbox:Rookie Walkthrough

**VulnHub Link:** [Funbox:Rookie](https://www.vulnhub.com/entry/funbox-rookie,520/)
**Difficulty:** Easy
**Release Date:** 27 Jul 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

ftp anonymous login allowed 

all zip files get 


```bash
ip2john *.zip ftp-zips.hash
ohn ftp-zips.hash
```

john password found --> unzipping and id_rsa file found

ssh connection successul ---> ssh tom@192.168.100.96 -i id_rsa_tom -t 'bash'

from mysql tom password found 

## 3.Privilege Escalation

linpeas executed and tom from sudo group

sudo bash and root flag captured.
