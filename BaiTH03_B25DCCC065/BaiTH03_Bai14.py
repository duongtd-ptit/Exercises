list_of_tuples = [(1, 2), (3, 4), (5, 6), (7, 8)]
def average_of_tuples(tuples):
    sum_x = 0
    sum_y = 0
    n = len(tuples)
    for t in tuples:
        sum_x += t[0]
        sum_y += t[1]
    avg_x = sum_x / n
    avg_y = sum_y / n
    return avg_x, avg_y
avg_x, avg_y = average_of_tuples(list_of_tuples)
print("Trung bình cộng của tất cả x là:", avg_x)
print("Trung bình cộng của tất cả y là:", avg_y)