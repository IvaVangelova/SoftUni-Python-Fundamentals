""" Checking words, are they palindrome """
words = input().split()
palindrome_word = input()
palindrome_list = [word for word in words if word == word[::-1]]
counter = palindrome_list.count(palindrome_word)
print(palindrome_list)
print(f'Found palindrome {counter} times')
