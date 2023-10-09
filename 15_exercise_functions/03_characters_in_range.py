def string_with_characters(first: str, second: str) -> list:
    """ Returns a list of string_characters """
    characters_list = []
    for character in range(ord(first) + 1, ord(second)):
        characters_list.append(chr(character))
    return characters_list


first_character = input()
second_character = input()
characters_in_list = string_with_characters(first_character, second_character)
print(" ".join(characters_in_list))
