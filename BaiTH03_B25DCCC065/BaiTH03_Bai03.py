list_num = []
n = int(input("Nhập số lượng phần tử trong list: "))
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    list_num.append(num)
max_num = max(list_num)
print("Số lớn nhất trong list là:", max_num)