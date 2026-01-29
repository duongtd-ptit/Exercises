try:
    a = int(input("Nhập số a: "))
    b = int(input("Nhập số b: "))
    result = a / b
except ZeroDivisionError:   #Thực hiện khi xảy ra lỗi
    print("Không thể chia cho 0!")
else:   #Thực hiện khi không có lỗi
    print("Kết quả =", result)
finally:    #Luôn thực hiện
    print("Chương trình kết thúc.")