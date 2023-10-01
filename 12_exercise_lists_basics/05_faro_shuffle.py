deck_of_cards = input().split()
faro_shuffles = int(input())

for i in range(faro_shuffles):

    new_deck_after_shuffles = []
    split_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[:split_deck]
    right_part = deck_of_cards[split_deck:]

    for shuffle in range(len(left_part)):

        new_deck_after_shuffles.append(left_part[shuffle])
        new_deck_after_shuffles.append(right_part[shuffle])
        deck_of_cards = new_deck_after_shuffles

print(new_deck_after_shuffles)

