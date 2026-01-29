dct_1 = {}
dct_2 = {}
def them_dct_1():
    x = input("Nhap key: ")
    y = int(input(f"Nhap value cua {x}: "))
    dct_1[x] = y
def them_dct_2():
    x = input("Nhap key: ")
    y = int(input(f"Nhap value cua {x}: "))
    dct_2[x] = y
def gop_2_dict():
    for i in dct_1:
        if i not in dct_2:
            dct_2[i] = dct_1[i]
        else:
            dct_2[i] += dct_1[i]
    for i in dct_2:
        print(f"{i} : {dct_2[i]}")        
while True:
    a = int(input("1 : Them du lieu vao dict_1\n2 : Them du lieu vao dict_2\n3 : Gop 2 dict tao thanh dict moi\nNhap so cua ban: "))
    if a == 1:
        print("Them du lieu vao dict_1")
        them_dct_1()
        print()
    elif a ==2:
        print("Them du lieu vao dict_2")
        them_dct_2()
        print()
    elif a == 3:
        print("Gop hai dict")
        gop_2_dict()
        break
    else:
        print("So khong hop le, hay thu lai")