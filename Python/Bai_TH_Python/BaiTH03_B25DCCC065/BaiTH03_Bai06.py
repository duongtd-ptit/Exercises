list = [1, 2, 3, 4, 5]
def reverse_list(list):
    reversed_lst = []
    for i in range(len(list)-1, -1, -1):
        reversed_lst.append(list[i])
    return reversed_lst
print("List ban đầu:", list)
print("List sau khi đảo ngược:", reverse_list(list))