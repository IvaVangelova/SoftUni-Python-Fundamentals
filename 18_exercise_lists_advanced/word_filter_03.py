""" Check if word is even"""


def even_word(list_words: list):
    """ Check every word in list """
    for word in list_words:
        if len(word) % 2 == 0:
            print(word)


words = input().split()
even_word(words)
