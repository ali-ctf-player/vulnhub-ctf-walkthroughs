

# Tr0ll:1 Walkthrough 

**VulnHub Link:** [Tr0ll:1](https://www.vulnhub.com/entry/tr0ll-1,100/)
**Difficulty:** Easy
**Release Date:** 14 Aug 2014

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```


ftp anonymous login ---> lol.pcap --> sup3rs3cr3tdirlol in url and roflmao found

strings roflmao ---> 0x0856BF found

Pass.txt and usernames found

overflow:Pass.txt found

## 3.Post Exploitation

ssh login ---> linpeas.sh ----> Linux 3.13.0 < 3.19 exploit found

escalating to root and root flag captured.
