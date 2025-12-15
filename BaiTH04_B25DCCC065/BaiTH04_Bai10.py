lst = list(map(int,input("Nhap cac so nguyen duong cach nhau boi dau cach: ").split()))
new_lst = []
for i in lst:
    if i %2 == 0 and i >10:
        new_lst.append(i)
print(f"List moi cua ban la: {new_lst}")