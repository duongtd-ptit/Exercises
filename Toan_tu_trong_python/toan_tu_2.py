a = int(input("Nhập số may mắn hôm nay trong dãy số chia hết cho 5 mà nhỏ hơn 100: "))
b = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95]
c = 30
if a in b:
    print("Hãy chờ thời gian để quay số")
    if a==c:
        print("Chúc mừng bạn đã trúng giải đặc biệt")
    else:
        print("Rất tiếc bạn chưa trúng giải đặc biệt")
else:
    print("Số bạn nhập không hợp lệ")

