# Level 01

Just like the previous level, there is nothing interesting in the home folder of the user `level01`, so we need to find a way to get the password of the user `flag01`, after some enumeration we found the password in the file `/etc/passwd` as shown below

```bash
level01@SnowCrash:~$ cat /etc/passwd | grep -w flag01
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
level01@SnowCrash:~$
```

The password is stored in an encrypted form, we can use `john` to crack it

```bash
level01@SnowCrash:~$ cat /etc/passwd | grep flag01 | cut -d ':' -f2
42hDRfypTqqnw

# on our attack box
❯ john hash
Loaded 1 password hash (descrypt, traditional crypt(3) [DES 128/128 SSE2])
Press 'q' or Ctrl-C to abort, almost any other key for status
abcdefg          (?)
1g 0:00:00:00 100% 2/3 100.0g/s 76800p/s 76800c/s 76800C/s raquel..bigman
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```
Now we can use the password to login as `flag01` and get the token






