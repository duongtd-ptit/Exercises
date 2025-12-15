dct = {}
def them_key():
    print("Them key moi vao trong dict")
    input_key = input("Nhap key: ")
    input_value = input(f"Nhap gia tri cua {input_key}: ")
    dct[input_key] = input_value
    print("*"*30)
them_key()
while True:
    a = int(input(f"Nhap 1 de tiep tuc them key\nNhap 2 de dung lai va in ra toan bo du lieu\n\nNhap so: "))
    if a == 1:
        them_key()
    if a == 2:
        for i in dct:
            print("Cac gia tri trong dict:")
            print(f"{i}-->{dct[i]}")
        break    