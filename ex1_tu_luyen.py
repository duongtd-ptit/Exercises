#yêu cầu người dùng nhập một câu
sentence = input("Nhập một câu bất kỳ mà bạn muốn: ")
#khởi tạo bộ đếm
lower_count = 0 #chữ thường
digit_count = 0 #chữ số

for char in sentence:
    if char.islower():
        lower_count += 1 #số lượng chữ thường +1
    elif char.isdigit():
        digit_count += 1 #số lượng chữ số +1

print("Số lượng chữ thường trong câu là:", lower_count)
print("Số lượng chữ số trong câu là:", digit_count)

length = len(sentence)

if length >=10 and "@" not in sentence and "!" not in sentence:
    print("Chuỗi này hợp lệ")
elif length <10:
    print("Chuỗi này không hợp lệ vì độ dài phải ít nhất 10 ký tự")
else:
    print("Chuỗi này không hợp lệ vì không được chứa ký tự đặc biệt '@' hoặc '!'")