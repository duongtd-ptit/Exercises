#Bắt lỗi tổng quát:
try:
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    print("Ket qua cua a/b: ",a/b)
except:
    print("Gia tri ban nhap da xay ra loi!!")
    
#Bắt lỗi cụ thể:    
try:
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    print("Ket qua cua a/b: ",a/b)
except ZeroDivisionError:
    print("Khong the chia cho 0")
except ValueError:
    print("Vui long nhap so hop le")

#Bắt nhiều lỗi một lúc
try:
    x = int("abc")
    y = 10 / 0
except (ValueError, ZeroDivisionError):
    print("Đã có lỗi về giá trị hoặc phép chia cho 0!")