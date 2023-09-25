lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken_count = 0
sword_broken_count = 0
shield_broken_count = 0
armor_broken_count = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        helmet_broken_count += 1
    if i % 3 == 0:
        sword_broken_count += 1
    if i % 2 == 0 and i % 3 == 0:
        shield_broken_count += 1
        if shield_broken_count % 2 == 0:
            armor_broken_count += 1

expenses = helmet_broken_count * helmet_price \
           + sword_broken_count * sword_price \
           + shield_broken_count * shield_price \
           + armor_broken_count * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
