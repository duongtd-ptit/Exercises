f = open("data.txt","r",encoding="utf-8")
content = f.read()
print(content)
f.close()


f = open("data.txt","r",encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

f = open("data.txt","r",encoding="utf-8")
print(f.readline())
print(f.readlines())
f.close()