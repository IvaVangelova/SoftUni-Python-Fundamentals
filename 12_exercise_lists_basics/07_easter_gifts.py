names_of_gifts = input().split()
command_and_gift = input()

while "No Money" not in command_and_gift:

    command_and_gift = command_and_gift.split()

    if "OutOfStock" in command_and_gift:
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == command_and_gift[1]:
                names_of_gifts[i] = "None"
    elif "Required" in command_and_gift:
        for j in range(len(names_of_gifts)):
            if j == int(command_and_gift[2]):
                names_of_gifts[j] = command_and_gift[1]
    elif "JustInCase" in command_and_gift:
        names_of_gifts[-1] = command_and_gift[1]

    command_and_gift = input()

while "None" in names_of_gifts:
    names_of_gifts.remove("None")
print(' '.join(names_of_gifts))

