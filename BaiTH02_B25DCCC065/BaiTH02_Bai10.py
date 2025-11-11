def reverse_list():
    user_input = input("Vui lòng nhập danh sách các số, cách nhau bởi dấu cách (Ví dụ: 10 20 30 40 50): ")
    str_numbers = user_input.split()
    if not str_numbers:
        print("\nBạn chưa nhập số nào. Vui lòng thử lại.")
        return
    try:
        original_list = [int(s) for s in str_numbers]
    except ValueError:
        print("\nLỗi: Danh sách nhập vào chứa giá trị không phải là số nguyên.")
        return
    print("\n" + "=" * 50)
    print(f"Danh sách ban đầu: {original_list}")
    print("-" * 50)
    reversed_list_slicing = original_list[::-1]
    print(f"Danh sách đảo ngược (Slicing):    **{reversed_list_slicing}**")
reverse_list()