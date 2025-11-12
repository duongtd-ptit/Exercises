my_tuple_1 = (1,2,3,4,5) #giống list những không thể thay đổi phần tử sau khi tạo
single = (1,) #1 phần tử vẫn phải để dấu ,
print(my_tuple_1[0])
print(my_tuple_1[2])
print("="*30)

my_tuple_2 = ('a','b','c','d','e','f','g','h')
print(my_tuple_2[0:3:1]) #tuple[start:end:step]
print(my_tuple_2[0:7:2])
print("="*30)
for word in my_tuple_2: #vẫn lấy được các phần tử dù là bất biến
    print(word)
print(f'Chiều dài của Tuple: {len(my_tuple_2)}')
print(f"Số lần xuất hiện của giá trị 'a': {my_tuple_2.count('a')}")
my_tuple = my_tuple_1 + my_tuple_2
print(my_tuple)
new_tuple = my_tuple*2
print(new_tuple)
print('ebe' in my_tuple) #kiểm tra xem giá trị có tồn tại trong dữ liệu bất biến không