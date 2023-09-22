counter_breads = 0
counter_color_eggs = 0
budget = float(input())
price_per_kg_flour = float(input())
while True:
    price_pack_eggs = price_per_kg_flour * 0.75
    price_per_liter_milk = price_per_kg_flour * 1.25
    total_price_per_bread = price_per_kg_flour + price_pack_eggs + (price_per_liter_milk / 4)
    if total_price_per_bread > budget:
        break
    if budget > total_price_per_bread:
        budget -= total_price_per_bread
        counter_breads += 1
        counter_color_eggs += 3
        if counter_breads % 3 == 0:
            counter_color_eggs -= (counter_breads - 2)
print(f"You made {counter_breads} loaves of Easter bread! "
      f"Now you have {counter_color_eggs} eggs and {budget:.2f}BGN left.")
