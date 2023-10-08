items_with_prices = [s for s in input().split("|")]
budget = float(input())
train_ticket = 150
exceed_clothes_price = 50.00
exceed_shoes_price = 35.00
exceed_accessories_price = 20.50
is_in_exceed_price = False
markup_price = 0
total_sold_items = 0
sold_items_list = []
for item in items_with_prices:

    type_item, item_price = item.split("->")
    item_price = float(item_price)
    if item_price > budget:
        continue
    if type_item == "Clothes" and item_price < exceed_clothes_price:
        budget -= item_price
        markup_price = item_price * 1.40
        is_in_exceed_price = True
    elif type_item == "Shoes" and item_price < exceed_shoes_price:
        budget -= item_price
        markup_price = item_price * 1.40
        is_in_exceed_price = True
    elif type_item == "Accessories" and item_price < exceed_accessories_price:
        budget -= item_price
        markup_price = item_price * 1.40
        is_in_exceed_price = True
    total_sold_items += markup_price
    sold_items_list.append(markup_price)
    is_in_exceed_price = False
print(f"{(sold_items_list):.2f}")