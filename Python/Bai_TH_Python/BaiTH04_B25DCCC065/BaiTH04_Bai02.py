i = tuple(map(int,input("Nhap cac so ban muon them vao TUPLE cach nhau boi dau cach: ").split()))
j = int(input("Nhap so ban muon kiem tra so lan xuat hien trong TUPLE: "))
print(f"So lan xuat hien cua {j} la: {i.count(j)}")