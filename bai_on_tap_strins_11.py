s = input("Nhập chuỗi cần chuẩn hoá:").strip()
s_split = s.split()
final_s = " ".join(s_split).capitalize()
print("Chuỗi của bạn sau khi chuẩn hoá là:", final_s)