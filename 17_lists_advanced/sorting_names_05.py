""" Sorting names, by length """


def sorting(names_list: list) -> list:
    """ Sorting list """
    names_list.sort()
    sorted_list = sorted(names_list, key=len, reverse=True)
    return sorted_list


names = input().split(", ")
result = sorting(names)
print(result)
