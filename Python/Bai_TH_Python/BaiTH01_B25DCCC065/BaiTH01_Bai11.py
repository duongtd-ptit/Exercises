n = int(input("Bạn muốn xem bảng cửu chương của số: "))
s=0
print(f"Bảng cửu chương của số {n} là:")
for i in range(1,10):
    s=n*i
    print(f"{n}x{i}={s}".center(20))