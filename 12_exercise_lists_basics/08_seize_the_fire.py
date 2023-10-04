cells = input().split("#")
total_water = int(input())
effort = 0
high_range = range(81, 126)
medium_range = range(51, 81)
low_range = range(1, 51)
is_in_range = False
fire_cells = []
total_fire_put_out = 0

for cell in cells:

    type_of_level, value = cell.split(" = ")
    value = int(value)
    is_in_range = False

    if type_of_level == "Low":
        if value in low_range:
            is_in_range = True
    elif type_of_level == "Medium":
        if value in medium_range:
            is_in_range = True
    elif type_of_level == "High":
        if value in high_range:
            is_in_range = True
    if is_in_range:
        if value + total_fire_put_out <= total_water:
            total_fire_put_out += value
            fire_cells.append(str(value))
            effort += value * 0.25

print("Cells:")
for fire_cell in fire_cells:
    print(f" - {fire_cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_put_out}")
