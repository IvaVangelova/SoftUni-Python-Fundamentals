team_a = (["A-" + str(s) for s in range(1, 12)])
team_b = (["B-" + str(s) for s in range(1, 12)])
red_cards = input().split()
is_terminated = False
for i in red_cards:
    if i in team_a:
        team_a.remove(i)
    elif i in team_b:
        team_b.remove(i)
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")
