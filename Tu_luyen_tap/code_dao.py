a,b,c = map(int,input().split())
if b>a:
    if c>b:
        print(c)
    else:
        print(b)
elif c>a:
    if b>c:
        print(b)
    else:
        print(c)
else:
    print(a)