def filter_list_greater_than_ten():
    user_input = input("Nhập danh sách các số (cách nhau bởi dấu cách): ")
    str_numbers = user_input.split()
    if not str_numbers:
        print("Không có số nào để phân tích.")
        return
    try:
        numbers = [int(s) for s in str_numbers]
    except ValueError:
        print("Lỗi: Đầu vào không phải là số nguyên hợp lệ.")
        return
    new_list = [num for num in numbers if num > 10]
    print("\n" + "=" * 40)
    print(f"Danh sách ban đầu: {numbers}")
    print("-" * 40)
    print(f"Danh sách mới (chỉ chứa các số > 10): **{new_list}**")
    print("=" * 40)
filter_list_greater_than_ten()