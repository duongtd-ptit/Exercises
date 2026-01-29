elc = float(input("Nhập số kWh đã tiêu thụ: "))
sum = 0
while elc <=0:
    print("Số kWh tiêu thụ không hợp lệ")
    elc = float(input("Nhập số kWh đã tiêu thụ: "))
if elc <= 50:
    sum = elc * 1800
    print(f"Tổng số tiền điện bạn phải trả là: {sum}đ")
elif elc >=50 and elc <=100:
    sum = 50 * 1800 + (elc-50)*2000
    print(f"Tổng số tiền điện bạn phải trả là: {sum}đ")
else:
    sum = 50*(1800+2000)+ (elc-100)*2500
    print(f"Tổng số tiền điện bạn phải trả là: {sum}đ")