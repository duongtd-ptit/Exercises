lst = list(map(int,input("Nhap cac so cua ban: ").split()))
dct = {}
for i in lst:
    if i not in dct:
        dct[i] =1
    else:
        dct[i] +=1
for i in dct:
    print(f"So lan xuat hien cua {i} :{dct[i]} lan")