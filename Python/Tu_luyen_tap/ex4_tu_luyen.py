#Nhập tên người dùng đầy đủ
#Cấm từ khoá "admin" hoặc "root"
#Xoá khoảng trắng ở hai đầu nếu có

name = input("Nhập họ và tên đầy đủ của bạn: ")
check_name = name.lower().strip()

while "admin" in check_name or "root" in check_name:
    print("Tên không được chứa từ khoá 'admin' hoặc 'root'. Vui lòng nhập lại.")
    name = input("Nhập họ và tên đầy đủ của bạn: ")
    check_name = name.lower().strip()
print("Tên sau chuẩn hoá của bạn là: ", check_name.title())
