s = input("Hãy nhập chuỗi bạn cần xoá ký tự: ").lower()
s1 = input("Hãy nhập các ký tự bạn muốn xoá: ").lower()
new_s = s.replace(s1, "",1)
print("Chuỗi S cuối cùng sau khi xoá các ký tự đó là:",new_s.capitalize())