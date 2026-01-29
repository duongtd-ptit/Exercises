def remove_duplicates():
    user_input = input("Vui lòng nhập danh sách các số, cách nhau bởi dấu cách (Ví dụ: 1 2 2 3 4 4 5 1): ")
    str_numbers = user_input.split()
    if not str_numbers:
        print("\nBạn chưa nhập số nào. Vui lòng thử lại.")
        return
    try:
        numbers = [int(s) for s in str_numbers]
    except ValueError:
        print("\nLỗi: Danh sách nhập vào chứa giá trị không phải là số nguyên.")
        return
    unique_set = set(numbers) 
    unique_list = list(unique_set) 
    print("\n" + "=" * 50)
    print(f"Danh sách ban đầu: {numbers}")
    print("-" * 50)
    print(f"Danh sách sau khi loại bỏ trùng lặp: **{unique_list}**")
    print("=" * 50)
remove_duplicates()