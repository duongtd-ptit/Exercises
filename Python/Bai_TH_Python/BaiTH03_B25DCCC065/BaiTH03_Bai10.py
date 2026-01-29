list = [1, 2, 2, 3, 4, 4, 5, 1, 3, 4, 4, 4]
def most_frequent(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_count = 0
    most_frequent_item = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent_item = item
    return most_frequent_item, max_count
item, count = most_frequent(list)
print("Phần tử xuất hiện nhiều nhất là:", item)
print("Số lần xuất hiện:", count)