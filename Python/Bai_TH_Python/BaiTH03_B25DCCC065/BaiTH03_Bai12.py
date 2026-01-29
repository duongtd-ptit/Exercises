input_string = input("Nhập một chuỗi: ")
frequency_dict = {}
for char in input_string:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
print("Dictionary đếm ký tự:", frequency_dict)