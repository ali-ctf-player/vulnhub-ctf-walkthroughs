

# Weakness:1 Walkthrough

**VulnHub Link:** [Weakness:1](https://www.vulnhub.com/entry/w34kn3ss-1,270/)
**Difficulty:** Medium 
**Release Date:** 14 Aug 2018

---

## 1. Reconnaissance

### Nmap Scan
```bash
nmap -A -O -T4 -P -sV 192.168.100.169

sudo echo "192.168.100.169    weakness.jth" > /etc/hosts
```

## 2. Web Enumeration
```
ffuf -c -ic -u 'http://weakness.jth/FUZZ' -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
```
/private found

from private we obtain my-key.pub and notes.txt

found out that my-key.pub is ssh_rsa key 


