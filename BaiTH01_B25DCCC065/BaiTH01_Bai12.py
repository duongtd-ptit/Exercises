n = int(input("Nhập số bạn muốn tính tổng từ 1 đến số đó: "))
sum =0
for i in range(1,n+1):
    sum+=i
    i+=1
print("Tổng của dãy đó là: ",sum)