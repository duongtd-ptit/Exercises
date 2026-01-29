from random import randint
running = True
while running:
    i = randint(1,10)
    number = int(input("Nhập số ngẫu nhiên từ 1-10: "))
    if number == i:
        print(f"Bạn đã trúng giải đặc biệt với số may mắn là {i}")
        break
    else:
        print("Hãy thử lại!!\n")
        continue