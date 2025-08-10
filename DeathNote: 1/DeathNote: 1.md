
# DeathNote: 1 Walkthrough

**VulnHub Link:** [DeathNote: 1](https://www.vulnhub.com/entry/deathnote-1,739/)
**Difficulty:** Easy
**Release Date:** 4 Sep 2021

## 1.Reconnaissance
nmap -A -O -T4 -P -sV 192.168.100.121


## 2. Enumaration 
dirb http://deathnote.vuln

on uploads page, we found usernames and notes 

## 3. Explotation 

bruteforce with hydra to ssh service --> hydra -L usernames.txt -P pass.txt ssh://192.168.100.121/ -I

l:death4me found

l and kira users found 

in /opt, case.wav and hint files found

in CyberChef kira user's password found --> kiraisevil

kira can run ALL commands as root

root flag captured.
