def ghi_list_ra_file(lst, ten_file):
    with open(ten_file, 'w', encoding='utf-8') as f:
        for item in lst:
            f.write(str(item) + '\n')