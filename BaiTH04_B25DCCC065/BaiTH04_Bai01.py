i = list(map(int,input("Nhap cac so cach nhau boi dau cach: ").split()))
sum = 0
for j in i:
    sum+=j
print(f"List cua ban la: {i}")    
print(f"Tong cac so trong list la: {sum}")