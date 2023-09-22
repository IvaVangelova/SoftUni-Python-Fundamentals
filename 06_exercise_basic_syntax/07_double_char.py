command = input()
save = ''
while command != "End":
    if command != "SoftUni":
        for char in command:
            save += char * 2
        print(save)
        save = ''
    command = input()
