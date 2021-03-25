data = input()
def stock(data):
    elements=data.split()
    products = {
        elements[index]: int(elements[index+1])
        for index in range(0,len(elements),2)
    }

    return products
search_products = input().split()
procducts = stock(data)
for search_product in search_products:
    if search_product in procducts:
        quantity = procducts[search_product]
        print(f"We have {quantity} of {search_product} left")
    else:
        print(f"Sorry, we don't have {search_product}")