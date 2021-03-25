data = input()
def products(data):

    elements = data.split()
    products = {
        elements[index]: int(elements[index+1])
        for index in range(0,len(elements),2)
    }

    return products
print(products(data))