try:
    f = open("data.txt", "r", encoding="utf-8")
    try:
        content = f.read()
        print(content)
    except UnicodeDecodeError:
        print("Lỗi đọc mã hóa file!")
    finally:
        f.close()
except FileNotFoundError:
    print("Không tìm thấy file!")