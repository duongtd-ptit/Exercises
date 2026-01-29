diem=float(input("Nhập điểm của bạn: "))
if diem >= 9 and diem <=10:
    print("Xếp loại A+ và GPA 4.0")
elif diem >= 8.5 and diem <8.9:
    print("Xếp loại A và GPA 3.7")
elif diem >= 8 and diem <8.4:
    print("Xếp loại A- và GPA 3.5")
elif diem >= 7 and diem <7.9:
    print("Xếp loại B+ và GPA 3.0")
elif diem >= 6.5 and diem <6.9: 
    print("Xếp loại B và GPA 2.7")
elif diem >= 6 and diem <6.4:
    print("Xếp loại B- và GPA 2.5")
elif diem >= 5 and diem <5.9:
    print("Xếp loại C+ và GPA 2.0")
elif diem >= 4.5 and diem <4.9:
    print("Xếp loại C và GPA 1.7")
elif diem >= 4 and diem <4.4:
    print("Xếp loại C- và GPA 1.5")
else:
    print("Xếp loại F và GPA 0.0")