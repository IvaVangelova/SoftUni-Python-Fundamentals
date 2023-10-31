def checking_cards(cards, number_of_commands):
    for _ in range(number_of_commands):
        command = input().split(", ")
        action = command[0]
        if action == "Add":
            card_name = command[1]
            if card_name in cards:
                print("Card is already in the deck")
            else:
                cards.append(card_name)
                print("Card successfully added")
        elif action == "Remove":
            card_name = command[1]
            if card_name not in cards:
                print("Card not found")
            else:
                cards.remove(card_name)
                print("Card successfully removed")
        elif action == "Remove At":
            index = int(command[1])
            if index not in range(len(cards)):
                print("Index out of range")
            else:
                cards.remove(cards[index])
                print("Card successfully removed")
        elif action == "Insert":
            card_name = command[2]
            index = int(command[1])
            if index not in range(len(cards)):
                print("Index out of range")
            elif card_name in cards:
                print("Card is already added")
            else:
                cards.insert(index, card_name)
                print("Card successfully added")
    return cards


deck_cards = input().split(", ")
numbers = int(input())
result = checking_cards(deck_cards, numbers)
print(", ".join(result))
