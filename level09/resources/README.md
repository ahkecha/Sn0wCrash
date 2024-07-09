# Level 09

Level 09 contains 2 files a binary and a token file.

```bash
level09@SnowCrash:~$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
level09@SnowCrash:~$
```

the binary takes a strings as argument and produces another string as output.


```bash
level09@SnowCrash:~$ ./level09 aaaa
abcd
level09@SnowCrash:~$ ./level09 bruh
bswk
```


let's try to understand what the binary does with our string and how it produces the output, from the above example we can see that the output is the input string with each character incremented by 1 depending on its position in the string, taking into consideration we can confirm that the token file is the output of the binary with the input string being the token.

opening the binary in BinaryNinja we can confirm our initial assumption, here is the pseudo code of the binary.

```c
080487ce  int32_t main(int32_t argc, char** argv, char** envp)

080487e3      void* gsbase
080487e3      int32_t eax_1 = *(gsbase + 0x14)
080487f2      int32_t var_11c = 0
080487fa      void* var_120 = 0xffffffff
08048828      void* eax_4
08048828      if (ptrace(request: PTRACE_TRACEME, 0, 1, 0) s< 0)
08048831          puts(str: "You should not reverse this")
08048836          eax_4 = 1
0804884e      else if (getenv(name: "LD_PRELOAD") != 0)
08048873          fwrite(buf: "Injection Linked lib detected ex…", size: 1, count: 0x25, fp: stderr)
08048878          eax_4 = 1
08048898      else if (open(file: "/etc/ld.so.preload", oflag: 0) s> 0)
080488bd          fwrite(buf: "Injection Linked lib detected ex…", size: 1, count: 0x25, fp: stderr)
080488c2          eax_4 = 1
080488db      else
080488db          int32_t eax_7 = syscall_open("/proc/self/maps", 0)
080488e9          if (eax_7 == 0xffffffff)
08048912              fwrite(buf: "/proc/self/maps is unaccessible,…", size: 1, count: 0x46, fp: stderr)
08048917              eax_4 = 1
08048a68          else
08048a68              while (true)
08048a68                  void var_114
08048a68                  eax_4 = syscall_gets(&var_114, 0x100, eax_7)
08048a6f                  if (eax_4 == 0)
08048a6f                      break
08048937                  if (isLib(&var_114, "libc") != 0)
08048939                      var_11c = 1
0804894b                  else if (var_11c != 0)
08048967                      if (isLib(&var_114, &data_8048c30) != 0)
08048971                          if (argc != 2)
08048a07                              eax_4 = fwrite(buf: "You need to provied only one arg…", size: 1, count: 0x22, fp: stderr)
08048996                          else
08048996                              while (true)
08048996                                  var_120 = var_120 + 1
080489b7                                  int32_t ecx_1 = 0xffffffff
080489bb                                  int32_t edi_1 = argv[1]
080489bd                                  while (ecx_1 != 0)
080489bd                                      bool cond:0_1 = 0 != *edi_1
080489bd                                      edi_1 = edi_1 + 1
080489bd                                      ecx_1 = ecx_1 - 1
080489bd                                      if (not(cond:0_1))
080489bd                                          break
080489c8                                  if (var_120 u>= not.d(ecx_1) - 1)
080489c8                                      break
08048991                                  putchar(c: sx.d(*(var_120 + argv[1])) + var_120)
080489da                              eax_4 = fputc(c: 0xa, fp: stdout)
0804896d                          break
08048a24                      if (afterSubstr(&var_114, "00000000 00:00 0") == 0)
08048a49                          eax_4 = fwrite(buf: "LD_PRELOAD detected through memo…", size: 1, count: 0x30, fp: stderr)
08048a4e                          break
08048a85      if (eax_1 == *(gsbase + 0x14))
08048a92          return eax_4
08048a87      __stack_chk_fail()
08048a87      noreturn
```

we can easily solve it with the following script.

```python

f = open("token", "rb")
token = f.read()

for i in range(0, len(token)):
   print(chr(abs(token[i] - i)), end="")

# output
# f3iji1ju5yuevaus41q1afiuq
```

use the token to log in as flag09.

```bash
level09@SnowCrash:~$ su flag09
Password:
Don't forget to launch getflag !
flag09@SnowCrash:~$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```





