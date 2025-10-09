for n in range (2,100):
    for i in range(2,n):
        if n % i ==0: #neu n chia het cho i
            print(f"{n} = {i} * {n//i}") #n bang i nhan voi phan nguyen cua n chia i
            break
    else : #neu khong co so n nao chia het cho i
        print(f"{n} la so nguyen to")