text1 = input("Hãy nhập một câu bằng tiếng anh bất kì mà bạn muốn: ")
text = text1.lower()
print("\n\nCâu của bạn là:",text)

if text.endswith("end") is True:
    print("\nCâu kết thúc đã bằng \"end\"")
else:
    print("\nCâu không có kết thúc bằng \"end\"")


if text.count("is") >=1:
    vi_tri_is = text.find("is") + 1
    print("\nVị trí xuất hiện từ \"is\" là từ số:",vi_tri_is)
    new_text = text.replace("is","are")
    print("\nThay thế toàn bộ từ \"is\" trong câu thành từ \"are\" ta được câu mới là:",new_text.capitalize()) 
else:
    print("\nKhông có từ \"is\" xuất hiện trong câu")

danh_sach = text.strip().split(" ")
so_luong_tu = text.strip().count(" ") + 1
print("\nCâu trên chuyển thành danh sách, ta sẽ được danh sách sau:",danh_sach)
print("\nSố lượng từ có trong câu là:",so_luong_tu)
    