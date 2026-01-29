#chỉ chứa số (0-9)
#chỉ chứa kí tự alphabet
#chỉ chứa số và kí tự alphabet
#tất cả kí tự đều viết hoa
#tất cả kí tự đều viết thường

check = input("Nhập nội dung bạn cần kiểm tra: ")
need_check = check.replace(" ","")
print("Chuỗi chỉ chứa số từ 0 đến 9:", need_check.isdigit())
print("Chuỗi chỉ chứa kí tự alphabet:", need_check.isalpha()) 
print("Chuỗi chứa cả chữ cái và chữ số:",need_check.isalnum())
print("Tất cả kí tự đều viết hoa:",need_check.isupper())
print("Tất cả đều viết thường:",need_check.islower())
