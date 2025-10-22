s1 = input("Chuỗi S1 mà bạn muốn là:")
s2 = input("Chuỗi S2 mà bạn muốn là:")
n = len(s1)
midde_text = n // 2
new_text = s1[:midde_text] + s2 + s1[midde_text:]
print("Khi chèn S2 vô giữa S1 ta có câu mới là:",new_text)