list_1 = list(map(int,input("Nhap cac so cua ban: ").split()))
list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(f"List ban dau:\n{list_1}")        
print(f"List moi loai bo phan tu trung lap, khong thay doi vi tri:\n{list_2}")