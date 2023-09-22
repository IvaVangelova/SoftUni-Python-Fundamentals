orders_count = int(input())
total_amount = 0
for i in range(orders_count):
    price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if 0.01 <= price <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        total_per_order = price * capsules_per_day * days
        total_amount += total_per_order
        print(f"The price for the coffee is: ${total_per_order:.2f}")
print(f"Total: ${total_amount:.2f}")
