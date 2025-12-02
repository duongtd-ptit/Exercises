def find_closest_pair(num_list, N):
    closest_sum = float('inf')
    closest_pair = ()
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            current_sum = num_list[i] + num_list[j]
            if abs(N - current_sum) < abs(N - closest_sum):
                closest_sum = current_sum
                closest_pair = (num_list[i], num_list[j])
    return closest_pair
numbers = [10, 22, 28, 29, 30, 40]
N = int(input("Nhập số N: "))
result = find_closest_pair(numbers, N)
print("Cặp phần tử có tổng gần nhất với {} là: {}".format(N, result))