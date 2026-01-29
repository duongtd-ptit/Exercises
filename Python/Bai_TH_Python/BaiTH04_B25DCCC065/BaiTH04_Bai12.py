lst = list(map(str,input("Nhap cac ten ban muon chuan hoa cach nhau boi dau ',': ").split(",")))
new_lst = []
for i in lst:
    a = i.title().strip()
    if a not in new_lst:
        new_lst.append(a)
for i in new_lst:
    print(f"Ten sau chuan hoa: {i}")