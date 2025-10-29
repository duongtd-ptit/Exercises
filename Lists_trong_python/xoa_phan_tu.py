animals = ["cat","dog","elephant","dolphin","duck","chicken","pig","monkey","frog","fish","turtle","crab","ant","crocodile","sea horse","horse","starfish","rabbit","mourse","shark","lion","tiger","sheep"]

del animals[2] #xoá phần tử theo vị trí bằng hàm del
print(animals)

popped_animal = animals.pop() #.pop xoá phần tử cuối cùng ở trong tập hợp / nếu .pop(i) thì xoá phần tử ở vị trí i
print(popped_animal)
print(animals)

removed_animal = animals.remove("dog") #remove sẽ xoá đi kí tự đầu tiên xuất hiện (remove sẽ xoá vĩnh viễn ptu đó)
print(animals)


original_animals = animals.copy()
print(original_animals)
reverse_animals = animals.reverse()
print(reverse_animals[1])