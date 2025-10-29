animals = ["cat","dog","elephant","dolphin","duck","chicken","pig","monkey","frog","shark","lion","tiger","sheep"]


original_animals = animals.copy()
print(original_animals)

animals.reverse() #đảo ngược vĩnh viễn bằng reverse
print(animals)

reversed_animals = animals[::-1] #đảo ngược tạm thời
print(reversed_animals)

sort_animals = animals
sort_animals.sort() #sắp xếp vĩnh viễn các phần tử
print(sort_animals)

sort_reverse_animals = animals
sort_reverse_animals.sort(reverse=True) #sắp xếp ngược
print(sort_reverse_animals)

sorted_animals = sorted(animals)
print(sorted_animals)