number_of_cities = int(input())
profit = 0
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_city = input()
    money_earned = float(input())
    expenses = float(input())

    if city % 3 == 0:
        profit = money_earned - (expenses + (expenses * 0.50))
    if city % 5 == 0:
        profit = (money_earned * 0.90) - expenses
    if city % 3 != 0 and city % 5 != 0:
        profit = money_earned - expenses
    total_profit += profit
    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
