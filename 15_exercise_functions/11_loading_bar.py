""" Build a loading bar """


def loading_bar(some_number: int) -> str:
    """ Finding how full is the loading bar """
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"

    percent_symbol = some_number // 10
    return f"{some_number}% [{'%' * percent_symbol}{'.' * (10 - percent_symbol)}]\nStill loading..."


number = int(input())
print(loading_bar(number))
