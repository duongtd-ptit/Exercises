name =input("Nhập tên của bạn: ")
chucvu = input("Nhập chức vụ của: ").lower()
age = int(input("Nhập tuổi của bạn: "))

a =("lop truong").lower()
b =("lop pho").lower()
c =("Bi thu").lower()
d =("Pho bi thu").lower()

if chucvu==a and age >= 18:
    print("Chào mừng", chucvu+ ", bạn đã đủ điều kiện tham gia")
    print("Chào mừng",name,"đã đến với chúng tôi")
elif chucvu==a and age < 18:
    print("Chào mừng", chucvu+ ", bạn không đủ điều kiện tham gia")
    print("xin lỗi",name+", hãy trở lại khi đủ tuổi nhé")
elif chucvu==b and age >= 18:
    print("Chào mừng", chucvu + ", bạn đã đủ điều kiện tham gia")
    print("Chào mừng",name,"đã đến với chúng tôi")
elif chucvu==b and age < 18:
    print("Chào mừng", chucvu+ ", bạn không đủ điều kiện tham gia")
    print("xin lỗi",name+", hãy trở lại khi đủ tuổi nhé")
elif chucvu==c and age >= 18:  
    print("Chào mừng", chucvu+ ", bạn đã đủ điều kiện tham gia")
    print("Chào mừng",name,"đã đến với chúng tôi")
elif chucvu==c and age < 18:
    print("Chào mừng", chucvu+ ", bạn không đủ điều kiện tham gia")
    print("xin lỗi",name+", hãy trở lại khi đủ tuổi nhé")
elif chucvu==d and age >= 18:
    print("Chào mừng", chucvu+ ", bạn đã đủ điều kiện tham gia")
    print("Chào mừng",name,"đã đến với chúng tôi")
elif chucvu==d and age < 18:
    print("Chào mừng", chucvu+ ", bạn không đủ điều kiện tham gia")
    print("xin lỗi",name+", hãy trở lại khi đủ tuổi nhé")
else:
    print("Bạn không phải là cán sự của lớp, bạn không được tham gia")