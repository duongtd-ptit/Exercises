product =  {"id": 1001, "name":"keybord","price":"500" }

print(f"Name item: {product['name']}")
print(f"Price: ${product['price']}")
print(f"Discription: {product.get('discription','NO DISCRIPTION')}")


people = {
    "p1": {"name": "John", "age": 30},
    "p2": {"name": "Jane", "age": 25}
}
print(people["p1"]["name"])
print(people["p2"]["age"])