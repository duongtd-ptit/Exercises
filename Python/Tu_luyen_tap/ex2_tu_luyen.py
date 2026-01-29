#Tạo một mk ngẫu nhiên gồm 8 kýtuwj
#sử dụng vòng lặp chạy 8 lần
#quy tắc xen kẽ: lần chẵn thêm một ký tự thường, lần lẻ thêm một số ngẫu nhiên

import random
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

password =""

for i in range(8):
    if i % 2 == 0:
        password += random.choice(letters)
    else:
        password += random.choice(digits)

print("Mật khẩu ngẫu nhiên được tạo là:", password)