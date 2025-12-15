def doc_du_lieu(ten_file):
    lst_tuple = []
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) >= 2:
                    ten = parts[0]
                    diem = float(parts[1])
                    lst_tuple.append((ten, diem))
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{ten_file}'")
        print("Bạn hãy kiểm tra lại đường dẫn hoặc vị trí file nhé.")
        return []
    return lst_tuple
def tong_hop_diem(lst_tuple):
    temp_dict = {}
    for name, score in lst_tuple:
        if name not in temp_dict:
            temp_dict[name] = []
        temp_dict[name].append(score)
    result_dict = {}
    for name, scores in temp_dict.items():
        avg_score = sum(scores) / len(scores)
        result_dict[name] = avg_score   
    return result_dict
def ghi_ket_qua(dct, ten_file_out):
    try:
        with open(ten_file_out, 'w', encoding='utf-8') as f:
            for name, avg in dct.items():
                f.write(f"{name}: {avg}\n")
        print(f"--> Đã ghi xong kết quả vào file '{ten_file_out}'")
    except Exception as e:
        print(f"Có lỗi khi ghi file: {e}")
# ==========================================
# --- PHẦN CHẠY CHƯƠNG TRÌNH (MAIN) ---
# ==========================================
file_dau_vao = "scores.txt"
file_dau_ra = "result.txt"
print("Đang đọc dữ liệu...")
du_lieu_tho = doc_du_lieu(file_dau_vao)

if du_lieu_tho:
    print("Đang tính điểm trung bình...")
    bang_diem_tb = tong_hop_diem(du_lieu_tho)
    ghi_ket_qua(bang_diem_tb, file_dau_ra)
    print("\nKết quả tính được là:")
    print(bang_diem_tb)