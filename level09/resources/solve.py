
f = open("token", "rb")
token = f.read()

for i in range(0, len(token)):
   print(chr(abs(token[i] - i)), end="")