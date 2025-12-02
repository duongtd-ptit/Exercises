def sum_all(*numbers):
    total = sum(numbers)
    print("Tổng =", total)
sum_all(1, 2, 3)
sum_all(4, 5, 6, 7)

def gioi_thieu(name):
    print(f"Xin chao {name}, rat vui duoc gap ban")
gioi_thieu(name=input("Nhap ten cua ban: "))