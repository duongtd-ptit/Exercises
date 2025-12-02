dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
def merge_dicts(d1, d2):
    merged_dict = d1.copy()  # Tạo bản sao của dict1 để không làm thay đổi dict1 ban đầu
    for key, value in d2.items():
        if key in merged_dict:
            merged_dict[key] += value  # Cộng giá trị nếu key đã tồn tại
        else:
            merged_dict[key] = value  # Thêm key mới nếu chưa tồn tại
    return merged_dict
merged = merge_dicts(dict1, dict2)
print("Dictionary sau khi gộp:", merged)