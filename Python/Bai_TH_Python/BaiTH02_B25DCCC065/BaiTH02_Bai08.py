def analyze_number_list():
    user_input = input("Vui lòng nhập một danh sách các số NGUYÊN, cách nhau bởi dấu cách (ví dụ: 10 5 -3 20): ")
    str_numbers = user_input.split()
    if not str_numbers:
        print("\nBạn chưa nhập số nào. Vui lòng thử lại.")
        return
    try:
        numbers = [int(s) for s in str_numbers]
    except ValueError:
        print("\nLỗi: Danh sách nhập vào chứa ký tự hoặc giá trị không phải là số nguyên hợp lệ.")
        print("Vui lòng chỉ nhập số nguyên và cách nhau bởi dấu cách.")
        return
    print("\n" + "=" * 40)
    print(f"Danh sách các số đã nhập: {numbers}")
    print("=" * 40)
    total_sum = sum(numbers)
    print(f"1. Tổng của danh sách là: **{total_sum}**")
    list_length = len(numbers)
    average = total_sum / list_length 
    print(f"2. Giá trị Trung bình là: **{average:.2f}**")
    max_number = max(numbers)
    print(f"3. Số lớn nhất trong danh sách là: **{max_number}**")    
    print("=" * 40)
analyze_number_list()