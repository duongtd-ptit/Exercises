def thong_ke_du_lieu(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            nums = [int(line.strip()) for line in f if line.strip().isdigit()] 
        if not nums:
            return (set(), None, None, 0)
        set_khong_trung = set(nums)
        so_lon_nhat = max(nums)
        so_nho_nhat = min(nums)
        trung_binh = sum(nums) / len(nums)
        return (set_khong_trung, so_lon_nhat, so_nho_nhat, trung_binh) 
    except FileNotFoundError:
        return None