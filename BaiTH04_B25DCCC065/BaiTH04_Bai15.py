def so_khop_du_lieu(id_da_nop, id_danh_sach_lop):
    sv_da_nop = id_da_nop & id_danh_sach_lop
    sv_chua_nop = id_danh_sach_lop - id_da_nop
    return (sv_da_nop, sv_chua_nop)
lop_hoc = {101, 102, 103, 104, 105}
da_nop = {101, 103, 999} 
ket_qua = so_khop_du_lieu(da_nop, lop_hoc)
ds_nop, ds_thieu = ket_qua
print(f"Danh sách lớp: {lop_hoc}")
print(f"Đã nộp: {ds_nop}")  
print(f"Chưa nộp: {ds_thieu}")