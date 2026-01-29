lst = list(map(float,input("Nhap cac so cua ban: ").split()))
max_num = float("-inf")
for i in lst:
    if i>=max_num:
        max_num = i
print(f"So lon nhat trong list la: {int(max_num)}")