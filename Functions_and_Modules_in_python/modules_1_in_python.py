a = float(input("Nhap so can tinh cua ban: "))

import math
print(math.sqrt(a)) #can bac 2
print(math.pi) #hang so pi
print("*"*30)

#import với bí danh
import math as m
print(m.pi)
print(m.pow(a,2)) #a mũ 2
print("*"*30)


#import cụ thể
from math import sqrt, pow
print(pow(a,2))
print(sqrt(a))