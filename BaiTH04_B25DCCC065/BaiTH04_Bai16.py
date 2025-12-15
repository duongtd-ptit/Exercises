def dem_so_dong(ten_file):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return len(lines)
    except FileNotFoundError:
        return 0