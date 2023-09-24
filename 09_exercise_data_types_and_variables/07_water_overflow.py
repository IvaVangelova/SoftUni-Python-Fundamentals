number_of_lines = int(input())
tank = 255
enough_liters = 0
for i in range(number_of_lines):
    liters_of_water = int(input())
    if enough_liters + liters_of_water > tank:
        print('Insufficient capacity!')
    if enough_liters + liters_of_water <= tank:
        enough_liters += liters_of_water
print(enough_liters)
