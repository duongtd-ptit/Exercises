a = float(input())
b = float(input())

def tong(a,b):
    return a+b
sum = tong(a,b)
print(f"Tong = {sum}")
def kiem_tra_chan_le(sum):
    if sum %2==0:
        print("Tong la so chan")
    else:
        print("Tong la so le")

def kiem_tra_am_duong(sum):
    if sum > 0:
        print("Tong la so duong")
    elif sum <0:
        print("Tong la so am")
    else:
        print("Tong = 0")

kiem_tra_am_duong(sum)
kiem_tra_chan_le(sum)