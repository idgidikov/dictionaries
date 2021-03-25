products = {}
while True:
    command = input()
    if command == "statistics":
        break
    product_name, quantity = command.split(': ')
    if product_name in products:
        products[product_name]+= int(quantity)
        continue
    products[product_name]= int(quantity)
    
    
print("Products in stock:")
for product_name, quantity in products.items():
    print(f"- {product_name}: {quantity}")
print(f'Total Products: {len(products.keys())}')
print(f"Total Quantity: {sum(products.values())} ")