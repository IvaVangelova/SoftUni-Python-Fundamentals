""" Checking symbol in word """
word = [symbol for symbol in input() if symbol.lower() not in ['a', 'o', 'u', 'e', 'i']]

print("".join(word))
