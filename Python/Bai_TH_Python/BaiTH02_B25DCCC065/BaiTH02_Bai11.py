def sum_even_elements():
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
    even_numbers = [num for num in numbers if num % 2 == 0]
    total_even_sum = sum(even_numbers)
    print("\n" + "=" * 40)
    print(f"Danh sách ban đầu: {numbers}")
    print(f"Các số chẵn tìm thấy: {even_numbers}")
    print(f"Tổng các phần tử chẵn là: **{total_even_sum}**")
    print("=" * 40)
sum_even_elements()