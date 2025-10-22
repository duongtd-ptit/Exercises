s = input("Nhập chuỗi bất kì mà bạn mong muốn:")
sum = 0
digits_in_s = []

for char in s:
    if char.isdigit():
        digits_in_s.append(char)
        sum+=int(char)
if not digits_in_s:
    print("Come on, I'm so tired!")
else:
    print("Các số xuất hiện trong dãy là:"," ".join(digits_in_s))
    print("Tổng các chữ số đó là:",sum)