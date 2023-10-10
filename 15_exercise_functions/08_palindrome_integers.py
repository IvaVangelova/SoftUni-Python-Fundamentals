""" Check if strings are palindrome """


def is_palindrome(strings: str) -> bool:
    """ Check if current string is palindrome and return answer in bool """
    if strings == strings[::-1]:
        return True
    return False


some_string = input().split(", ")
for current_string in some_string:
    print(is_palindrome(current_string))
