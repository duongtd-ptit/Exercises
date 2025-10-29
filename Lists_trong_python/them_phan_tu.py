animals = ["cat", "dog","mouse","chicken","horse"]
print(animals)

animals.append("lion")
print(animals)

animals.extend(["shark","tiger"])
print(animals)

animals.insert(0,"turtle")
print(animals)

list_1=[0,1,2,3,4]
list_2=[5,6,7,8,9]
sum_list = list_1 + list_2
print(sum_list)

new_list = [element for list in [list_1, list_2] for element in list]
print(new_list)

import itertools
new_list = list(itertools.chain(list_1,list_2))
print(new_list)

list_3 = [*list_1,*list_2] #cộng hai list như bình thường
print(list_3)
list_4 = [list_1,list_2] #list bị lồng vào nhau
print(list_4)

my_list = list(map(lambda x: x+2, list_1)) #thay đổi bằng hàm map và lambda
print(my_list)

my_list_1 = [10,11,12,13]
for index, value in enumerate(my_list_1):
    my_list_1[index] = value + 2
print(my_list_1) 