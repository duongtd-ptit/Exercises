fruits = {"banana","apple","cherry",}
for fruit in fruits:
    print(fruit) #mỗi lần cho một thứ tự khác nhau vì set là unordered (không được sắp xếp)
print("="*30)
numbers = {1,2,3,4,5,6}
for n in numbers:
    if n%2==0:
        print(f"{n} là số chẵn") #set được kết hợp với điều kiện trong vòng lặp
print("="*30)
squares = {x**2 for x in range(1,6)} #set tạo mới từ vòng lặp (set comprehension)
print(squares)