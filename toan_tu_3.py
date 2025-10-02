a=int(input("Hãy nhập 4 chữ số của bạn để hệ thống giúp tính toán"))
b = a*5+100
c = a/2-10
d = b+c-1000

if d<0:
    print("Nay có lẽ không may mắn cho bạn rồi")
elif d==0:
    print("Hôm nay có vẻ bạn không có gì đặc sắc nhỉ")
else:
    print("Mức độ may mắn hôm nay của bạn là", d)