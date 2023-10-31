numbers = input().split()

while True:
    command = input()
    if command == "Finish":
        break
    command_parts = command.split()
    action = command_parts[0]
    if action == "Add":
        value = command_parts[1]
        numbers.append(value)
    elif action == "Remove":
        value = command_parts[1]
        if value in numbers:
            numbers.remove(value)
    elif action == "Replace":
        value = command_parts[1]
        replacement = command_parts[2]
        if value in numbers:
            index = numbers.index(value)
            numbers[index] = replacement
    elif action == "Collapse":
        value = command_parts[1]
        numbers = [number for number in numbers if int(number) >= int(value)]
print(" ".join(numbers))
