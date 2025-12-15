def gop_du_lieu_tuple(danh_sach_tuple):
    dct = {}
    for id_item,value in danh_sach_tuple:
        if id_item not in dct:
            dct[id_item] = [value]
        else:
            dct[id_item].append(value)
    ket_qua = []
    for id_item, danh_sach_value in dct.items():
        ket_qua.append((id_item,danh_sach_value))
    return ket_qua
input_data = [(1, 'a'), (2, 'b'), (1, 'c'), (3, 'd'), (2, 'e')]
output = gop_du_lieu_tuple(input_data)
print(f"Input: {input_data}")
print(f"Output: {output}") 