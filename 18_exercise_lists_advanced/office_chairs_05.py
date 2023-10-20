""" Check chairs in rooms """


def check_rooms(rooms: int):
    """ Checking the chairs if they are enough """

    total_left_chairs = 0
    list_strings = []

    for room in range(1, rooms + 1):

        chairs, visitors = input().split()

        if len(chairs) >= int(visitors):
            left_chairs = len(chairs) - int(visitors)
            total_left_chairs += left_chairs
        else:
            needed_chairs = int(visitors) - len(chairs)
            total_left_chairs -= needed_chairs
            list_strings.append(f"{needed_chairs} more chairs needed in room {room}")

    return f"Game On, {total_left_chairs} free chairs left" if total_left_chairs >= 0 else "\n".join(list_strings)


number_of_rooms = int(input())
print(check_rooms(number_of_rooms))
