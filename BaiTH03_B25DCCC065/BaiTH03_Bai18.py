products = [("A001", 5), ("A002", 3), ("A001", 2), ("A003", 7), ("A002", 4)]
def merge_products(product_list):
    merged_dict = {}
    for sku, quantity in product_list:
        if sku in merged_dict:
            merged_dict[sku] += quantity
        else:
            merged_dict[sku] = quantity
    merged_list = [(sku, quantity) for sku, quantity in merged_dict.items()]
    return merged_list
merged_products = merge_products(products)
print("Danh sách sản phẩm sau khi gộp SKU trùng:", merged_products)