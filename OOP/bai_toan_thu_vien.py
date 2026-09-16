danh_sach_sach = []
def them_sach(title, author):
    cuon_sach = {
        "title" : title,
        "author" : author
    }
    danh_sach_sach.append(cuon_sach)

def in_danh_sach_sach():
    if len(danh_sach_sach) == 0:
        print("Hien chua co sach nao trong danh sach.")
        return
    print("--- DANH SACH THONG TIN SACH ---")
    for i, sach in enumerate(danh_sach_sach,start=1):
        print(f"{i}. Ten sach: {sach['title']} | Tac gia: {sach['author']}")
        print("-------------------------")
        
        
them_sach("Dế Mèn Phiêu Lưu Ký", "Tô Hoài")
them_sach("Số Đỏ", "Vũ Trọng Phụng")
them_sach("Lập trình Python cơ bản", "John Doe")


in_danh_sach_sach()