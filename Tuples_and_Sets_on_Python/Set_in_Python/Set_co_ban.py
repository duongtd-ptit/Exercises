#set: là một tập hợp (collection) dùng để lưu trữ các phần tử duy nhất không trùng lặp và không có thứ tự
#khác với list hay tuple, set không quan tâm đến vị trí phần tử và tự động loại bỏ các giá trị trùng nhau
#không có thứ tự --> không thể truy cập bằng số (index)
#không có phần tử trùng lặp
#có thể thay đổi thêm xoá các phần tử
numbers = [1,2,3,4,5,6,1,1,1,2,3,4]
numbers_set = set(numbers)
print(f"{numbers_set}\t")
empty_set = set() #tạo set rỗng
fruits = {"apple","banana","apple"}
fruits_set = set(fruits)
fruits_set.add("cherry") #thêm 1 phần tử
fruits_set.update(["orange","banana"]) #thêm nhiều phần tử
print(fruits_set)