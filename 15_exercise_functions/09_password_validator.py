""" Check if password is correct """


def check_password(given_password: str):
    """ Searching errors in the password """
    problems_list = []
    if not 6 <= len(given_password) <= 10:
        problems_list.append("Password must be between 6 and 10 characters")
    if not given_password.isalnum():
        problems_list.append("Password must consist only of letters and digits")
    digit_counter = 0
    for character in given_password:
        if character.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        problems_list.append("Password must have at least 2 digits")
    return problems_list


password = input()
errors_in_password = check_password(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))
