def diem_trung_binh():
    cuoi_ky = float(input("Nhap diem cuoi ky: "))
    giua_ky = float(input("Nhap diem giua ky: "))
    thuong_xuyen_1 = float(input("Nhap diem thuong xuyen 1: "))
    thuong_xuyen_2 = float(input("Nhap diem thuong xuyen 2: "))
    chuyen_can = float(input("Nhap diem chuyen can: "))
    tb = cuoi_ky/2+giua_ky/5+thuong_xuyen_1/10+thuong_xuyen_2/10+chuyen_can/10
    return tb
def phan_loai(tb):
    value = ""
    if tb >= 8:
        value = "Gioi"
    elif tb >=6.5:
        value = "Kha"
    elif tb >=5:
        value = "Trung Binh"
    else:
        value = "Yeu"
    return value
def ket_qua():
    name = input("Nhap ten sinh vien: ")
    re_name = name.title().strip()
    diem_so = diem_trung_binh()
    xep_loai_ket_qua = phan_loai(diem_so)
    dct = {}
    dct[re_name]=xep_loai_ket_qua
    return dct
a = ket_qua()
print("="*30)
print(f"Ket qua cuoi cung: {a}")