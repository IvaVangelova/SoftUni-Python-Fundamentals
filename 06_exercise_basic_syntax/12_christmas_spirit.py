decorations_count = int(input())
days_left = int(input())
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
total_cost = 0
total_spirit = 0
for i in range(1, days_left + 1):
    if i % 11 == 0:
        decorations_count += 2
    if i % 2 == 0:
        total_cost += ornament_set * decorations_count
        total_spirit += 5
    if i % 3 == 0:
        total_cost += (tree_skirt + tree_garland) * decorations_count
        total_spirit += 13
    if i % 5 == 0:
        total_cost += tree_lights * decorations_count
        total_spirit += 17
        if i % 3 == 0:
            total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_garland + tree_lights
        if i == days_left:
            total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
