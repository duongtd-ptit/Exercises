n = int(input("Nhập số nguyên dương bất kì: "))
total = []
for i in range(0,n+1):
    if i%2==0:
        print(i)
        total.append(i)
print(f"Số số chẵn có trong dãy là: {len(total)}")