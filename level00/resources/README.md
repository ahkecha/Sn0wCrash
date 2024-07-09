# Level 00

Very straightforward level. We are given a user `level00` to get access to the machine, looking at the home folder there is nothing interesting, after some enumeration we found 2 files belonging the the user `flag00`, both are text files as shown below

```bash
level00@SnowCrash:~$ file $(find / -user flag00 2> /dev/null)
/usr/sbin/john:      ASCII text
/rofs/usr/sbin/john: ASCII text
level00@SnowCrash:~$ cat $(find / -user flag00 2> /dev/null)
cdiiddwpgswtgt
cdiiddwpgswtgt
level00@SnowCrash:~$
```
they contain a string `cdiiddwpgswtgt` which may be a candidate for the password of the user `flag00`, we can try to use it to login as `flag00` and get the token, but it doesn't work, so we need to find a way to use it as a password, after a while trying to make sense of that string we used cyberchef and found that its encoded in rot11
Now we can use the password "nottoohardhere" to login as `flag00` and get the token
