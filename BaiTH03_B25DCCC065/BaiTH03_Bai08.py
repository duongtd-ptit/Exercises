people = {}
for i in range(3):
    name = input("Nhập tên người thứ {}: ".format(i + 1))
    age = int(input("Nhập tuổi người thứ {}: ".format(i + 1)))
    people[name] = age 
print("Dictionary chứa tên và tuổi của 3 người:", people)