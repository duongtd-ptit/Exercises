list = [1, 2, 2, 3, 4, 4, 5, 1, 3]
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
print("List ban đầu:", list)
print("List sau khi loại bỏ phần tử trùng:", remove_duplicates(list))