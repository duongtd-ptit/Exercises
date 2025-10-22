S = input("Nhập vào chuỗi S (gồm các từ/số cách nhau bằng khoảng trắng): ")

# 1. Tách chuỗi S thành danh sách các từ
words = S.split()

# Khởi tạo danh sách để lưu TẤT CẢ các chuỗi có độ dài lớn nhất
max_list = []

# Khởi tạo độ dài lớn nhất hiện tại tìm được
max_length = 0

# 2. Duyệt qua TỪNG từ trong danh sách
for current_word in words:
    current_length = len(current_word)
    
    # Logic So sánh và Cập nhật
    if current_length > max_length:
        # Nếu tìm thấy chuỗi DÀI HƠN:
        # 1. Cập nhật độ dài lớn nhất
        max_length = current_length
        # 2. Xóa danh sách cũ và thêm chuỗi mới vào (vì chuỗi cũ không còn là lớn nhất nữa)
        max_list = [current_word]
        
    elif current_length == max_length:
        # Nếu tìm thấy chuỗi CÓ ĐỘ DÀI BẰNG NHƯNG CHƯA PHẢI LỚN NHẤT:
        # Thêm chuỗi đó vào danh sách
        max_list.append(current_word)

# 3. In kết quả cuối cùng
if not max_list:
    print("Chuỗi S không chứa từ nào hợp lệ (có thể là chuỗi rỗng).")
else:
    print(f"Các chuỗi con có độ dài lớn nhất ({max_length} ký tự) là:")
    
    # In tất cả các phần tử trong danh sách
    for item in max_list:
        print(f"- {item}")