year = int(input("Nhập năm mà bạn muốn kiểm tra"))
if year%400==0 or year%4==0 and year%100!=0:
    print("Năm của bạn là năm nhuận")
else:
    print("Năm của bạn không phải năm nhuận")