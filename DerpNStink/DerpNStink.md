

# DerpNStink Walkthrough 

**VulnHub Link:** [DerpNStink](https://www.vulnhub.com/entry/derpnstink-1,221/)
**Difficulty:** Easy
**Release Date:** 9 Feb 2018


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.139


## 2.Web Enumeration

dirb http://192.168.100.139


http://<ip>/index.html --> view page source and 256 SHA hash found and cracked  ---> Austrialia

url/webinfo.txt --> stinky user found

wpscan --url '<url>' -e ap,u --plugins-detection --> slideshow 1.4.6 vuln found

wp-admin --> admin:admin

reverse_shell.php uploaded and www-data shell opened

on mysql, stinky user's password found ---> wegdie57

from derpissues.pcap file , mrderp password found ---> derpderpderpderpderpderp

## 3.Privilege Escalation

sudo -l --> /home/mrderp/binaries/derpy

creating and echo 'chmod u+s /bin/bash' > derpy

executing and gaining root shell --> root flag captured.

flag1(52E37291AEDF6A46D7D0BB8A6312F4F9F1AA4975C248C3F0E008CBA09D6E9166)

flag2(a7d355b26bda6bf1196ccffead0b2cf2b81f0a9de5b4876b44407f1dc07e51e6)

flag3(07f62b021771d3cf67e2e1faf18769cc5e5c119ad7d4d1847a11e11d6d5a7ecb)

flag4(49dca65f362fee401292ed7ada96f96295eab1e589c52e4e66bf4aedda715fdd)
