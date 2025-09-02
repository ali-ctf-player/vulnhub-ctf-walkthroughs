
# Sunset:Daw Walkthrough 

**VulnHub Link:** [Sunset:Daw](https://www.vulnhub.com/entry/sunset-dawn,341/)
**Difficulty:** Easy
**Release Date:** 3 Aug 2019


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.139


## 2.Web Enumeration

dirb http://192.168.100.139


## 3.Exploitation

smbclient //192.168.100.139/ITDEPT -N

we have permission to upload

we copy bash reverse shell to file and upload to smbserver

we obtain www-data shell 

we upload linpeas to attack machine and observe that /usr/bin/zsh has suid byte

/usr/bin/zsh -p

and BOOOMM.!! Root flag captured

