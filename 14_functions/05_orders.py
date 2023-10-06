def calculate_order(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity


type_product = input()
product_quantity = int(input())
result = calculate_order(type_product, product_quantity)
print(f"{result:.2f}")
