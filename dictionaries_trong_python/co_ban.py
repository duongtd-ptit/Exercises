student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

print(student["name"])

value_1 = student.get("name")
print(value_1)
#value_2 = student.get(input("Nhập thông tin mà bạn cần tìm:"),"N/A") #Nhập key muốn tìm, nếu không có trả về N/A
#print(value_2)

student = {"name": "Alice", "age": 21}
print(student.keys())   # in toàn bộ key
print(student.values()) # in toàn bộ value
print(student.items())  # in key đi kèm với value của nó
