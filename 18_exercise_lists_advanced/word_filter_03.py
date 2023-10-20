words = input().split()
def even_word(list_words):
  for word in list_words:
    if len(word) % 2 == 0:
      print(word)
even_word(words)
