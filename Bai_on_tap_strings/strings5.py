name="      "+input("Nhập ten của bạn")+"     "
print(name.title()) #Viết hoa chữ cái đầu của mỗi từ
print(name.upper()) #Viết hoa tất cả các chữ cái
print(name.lower()) #Viết thường tất cả các chữ cái
print(name.capitalize()) #Viết hoa chữ cái đầu tiên của chuỗi
print(name.strip()) #Xoá khoảng trắng thừa ở đầu và cuối chuỗi
print(name.rstrip()) #Xoá khoảng trắng thừa ở cuối chuỗi
print(name.lstrip()) #Xoá khoảng trắng thừa ở đầu chuỗi

x = name.center(30,"!")
print(x)

print("Vị trí của 'D' là:", name.find("D"))
print(name.count("D"))
print(name.replace("D","@"))
print(name.replace("D","@",1)) #Thay thế 1 lần
print("D" in name) #Kiểm tra 'a' có trong chuỗi hay không
print("D" not in name) #Kiểm tra 'a' không có trong chuỗi hay không
print(name.startswith("D")) #Kiểm tra chuỗi có bắt đầu bằng 'D'
print(name.endswith("g")) #Kiểm tra chuỗi có kết thúc bằng 'g'
print(name.isalpha()) #Kiểm tra chuỗi có phải toàn chữ cái không
print(name.isdigit()) #Kiểm tra chuỗi có phải toàn số không
print(name.isspace()) #Kiểm tra chuỗi có phải toàn khoảng trắng không
print(name.islower()) #Kiểm tra chuỗi có phải toàn chữ thường không
print(name.isupper()) #Kiểm tra chuỗi có phải toàn chữ hoa không
print(name.istitle()) #Kiểm tra chuỗi có phải viết hoa chữ cái đầu của mỗi từ không
print(len(name)) #Độ dài của chuỗi