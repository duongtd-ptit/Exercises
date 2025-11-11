from collections import Counter
def find_most_frequent_element():
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
    counts = Counter(numbers)
    if counts:
        most_common_element, max_count = counts.most_common(1)[0]
    else:
        print("Danh sách rỗng.")
        return
    print("\n" + "=" * 40)
    print(f"Danh sách ban đầu: {numbers}")
    print(f"Phần tử xuất hiện nhiều nhất là: **{most_common_element}**")
    print(f"Số lần xuất hiện: **{max_count}** lần")
    print("=" * 40)

find_most_frequent_element()