def analyze_string():
    string1 = input("Nhập nội dung bạn muốn kiểm tra: ")
    string = string1.lower()
    if not string:
        print(f"\nChuỗi của bạn rỗng, hãy thử lại nhé!!")
        return
    print("*"*30)
    string_length = len(string)
    print(f"--Độ dài của chuỗi là-- {string_length}")
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    sorted_count = sorted(char_count.items())
    for char, count in sorted_count:
        print(f"\t--Kí tự \'{char}\' : {count} lần--")
analyze_string()