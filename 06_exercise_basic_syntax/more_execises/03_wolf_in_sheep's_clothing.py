animals = input()  # wolf, sheep, sheep, sheep, sheep, sheep
animal_list = animals.split(', ')  # sheep, sheep, wolf
animal_list.append('farmer')
animal_list.reverse()

for sheep in range(len(animal_list)):
    wolf = animal_list.index('wolf')
    if wolf == 1:
        print("Please go away and stop eating my sheep")
        break
    else:
        print(f'Oi! Sheep number {wolf - 1}! You are about to be eaten by a wolf!')
        break
