math = float(input("Nhập điểm Toán của bạn: "))
literature = float(input("Nhập điểm môn Văn của bạn: "))
english = float(input("Nhập điểm tiếng anh của bạn: "))

tb = (math+literature+english)/3
print(f"Điểm trung bình ba môn của bạn là: {round(tb,2)}")