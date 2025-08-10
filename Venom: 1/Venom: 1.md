
# Venom: 1 Walktrough

**VulnHub Link:** [Venom: 1](https://www.vulnhub.com/entry/venom-1,701/)
**Difficulty:** Easy
**Release Date:** 24 May 2021

## 1.Reconnaissance
nmap -A -O -T4 -P -sV 192.168.100.134
or with rustscan


## 2.Enumeration 

with enum4linux , usernames found

ftp service credentials --> hostinger:hostinger

>>> get hint.txt

>>> adding venom.box to hosts

>>> using base64, decoding them from hint.txt 

>>> using hostinger as key , decoding L7f9l8@J#p%Ue+Q1234 --> getting password for dora user : E7r9t8@Q#h%Hy+M1234

## 3. Exploitation

>>> python3 49876.py -u http://venom.box/panel/ -l dora -p E7r9t8@Q#h%Hy+M1234

>>> getting reverse shell with python and hostinger:hostinger again

>> in history ---> .htaccess , nathan passwword found --> FzN+f2-rRaBgvALzj*Rk#_JJYfg8XfKhxqB82x_a ---> flag captured

>>> sudo /bin/bash -i , escalating to root and flag captured
