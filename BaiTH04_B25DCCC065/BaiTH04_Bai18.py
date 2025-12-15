def doc_file_tao_dict(ten_file):
    ket_qua = {}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    name = parts[0]
                    score = int(parts[1]) 
                    
                    if name not in ket_qua:
                        ket_qua[name] = [score]
                    else:
                        ket_qua[name].append(score)
        return ket_qua
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tên là '{ten_file}'")
        print("Bạn hãy kiểm tra xem file đã nằm cùng thư mục với code chưa.")
        return {}
ten_file_cua_ban = "data.txt" 
ket_qua = doc_file_tao_dict(ten_file_cua_ban)
print("Kết quả đọc được là:")
print(ket_qua)