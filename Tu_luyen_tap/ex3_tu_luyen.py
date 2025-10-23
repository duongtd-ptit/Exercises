#Yêu cầu số nguyên dương từ người dùng
#Kiểm tra số đó có phải số nguyên tố hay không bằng vòng lặp While

num = int(input("Nhập một số nguyên dương bất kỳ: "))

while num <=1:
    print(num, "không phải là số nguyên tố.")
    num = int(input("Vui lòng nhập lại một số nguyên dương bất kỳ: "))
    if num == 2:
        print(num, "là số nguyên tố.")
    elif num > 2:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
if is_prime:
    print(num, "là số nguyên tố.")
else:
    print(num, "không phải là số nguyên tố.")


