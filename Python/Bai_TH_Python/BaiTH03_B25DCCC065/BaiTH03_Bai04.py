def check_key():
    my_key = ("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m")
    check_key = input("Nhap 1 ki tu muon kiem tra:  ") 
    if check_key in my_key:
        print(f"Ki tu {check_key} co trong tuple")
    else:
        print(f"Ki tu {check_key} khong co trong tuple")
check_key()