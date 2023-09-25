snowballs_count = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0
value = 0

for i in range(snowballs_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    value = (weight / time) ** quality
    if value > max_value:
        max_value = int(value)
        max_weight = weight
        max_time = time
        max_quality = quality

print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
