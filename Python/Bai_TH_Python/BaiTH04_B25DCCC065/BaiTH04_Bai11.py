lst = list(map(int, input("Nhap day cac so nguyen cach nhau boi dau cach: ").split()))
ket_qua = {}
for idx,value in enumerate(lst):
    if value not in ket_qua:
        ket_qua[value] = [idx]
    else:
        ket_qua[value].append(idx)
print(f"Input: {lst}")
print(f"Output: {ket_qua}")