lst = list(map(int,input("Nhap cac so ban cach nhau boi dau cach: ").split()))
sorted_lst = sorted(lst)
print(f"List cua ban sau sap xep la:\n{sorted_lst}")
print(f"Sau khi loai bo phan tu trung lap:\n{set(lst)}")