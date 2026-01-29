def merge_and_sort_lists():
    input1 = input("Nhập danh sách số thứ nhất (cách nhau bởi dấu cách): ")
    str_numbers1 = input1.split()
    input2 = input("Nhập danh sách số thứ hai (cách nhau bởi dấu cách): ")
    str_numbers2 = input2.split()
    try:
        list1 = [int(s) for s in str_numbers1]
        list2 = [int(s) for s in str_numbers2]
    except ValueError:
        print("Lỗi: Đầu vào chứa giá trị không phải là số nguyên.")
        return
    merged_list = list1 + list2
    merged_list.sort()
    print("\n" + "=" * 40)
    print(f"Danh sách 1: {list1}")
    print(f"Danh sách 2: {list2}")
    print("-" * 40)
    print(f"Danh sách đã gộp và sắp xếp: **{merged_list}**")
    print("=" * 40)
merge_and_sort_lists()