s = input("Hãy nhập chuỗi bạn cần xoá ký tự: ").lower()
s1 = input("Hãy nhập các ký tự bạn muốn xoá: ").lower()
new_s = s 
for char_need_remove in s1:
    new_s = new_s.replace(char_need_remove, "")
print(f"Chuỗi S cuối cùng sau khi xoá các ký tự đó là: {new_s}")