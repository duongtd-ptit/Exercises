def check_palindrome():
    original_string = input("Nhập chuỗi để kiểm tra tính đối xứng: ")
    processed_string = original_string.replace(" ","").lower()
    if not processed_string:
        print("\nChuỗi của bạn không hợp lệ, hãy thử lại nhé!!")
        return
    reversed_string = processed_string[::-1]
    print("*"*30)
    print(f"Chuỗi được chuẩn hoá: '{processed_string}'")
    print(f"Chuỗi đảo ngược: '{reversed_string}'")
    print("*"*30)
    if processed_string == reversed_string:
        print("Kết quả: CHUỖI ĐỐI XỨNG (Palindrome)")
    else:
        print("Kết quả: CHUỖI KHÔNG ĐỐI XỨNG")
check_palindrome()