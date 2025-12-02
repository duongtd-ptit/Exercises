original_list = [4, 15, 22, 8, 13, 6, 30, 7, 10, 12]
filtered_list = [num for num in original_list if num > 10 and num % 2 == 0]
print("List ban đầu:", original_list)
print("List sau khi lọc (số lớn hơn 10 và là số chẵn):", filtered_list)