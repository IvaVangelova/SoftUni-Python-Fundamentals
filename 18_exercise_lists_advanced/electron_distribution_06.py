number_of_electrons = int(input())
shells = []
for electron in range(1, number_of_electrons + 1):
    current_shell_max_electron = 2 * electron ** 2
    if current_shell_max_electron <= number_of_electrons:
        number_of_electrons -= current_shell_max_electron
        shells.append(current_shell_max_electron)
    else:
        shells.append(number_of_electrons)
        break
print(shells)
