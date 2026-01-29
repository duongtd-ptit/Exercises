list_num = []
n = int(input("Nhập số lượng phần tử trong list: "))
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    list_num.append(num)
total = sum(list_num)
print("Tổng tất cả phần tử trong list là:", total)