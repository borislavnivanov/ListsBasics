cards_list = str.split(input())

team_A: list = []
team_B: list = []
termination_flag = False

for element in cards_list:

    carton = str.split(element, '-')

    if carton[0] == 'A':
        if carton[1] not in team_A:
            team_A.append(carton[1])
    elif carton[0] == 'B':
        if carton[1] not in team_B:
            team_B.append(carton[1])

    if len(team_A) > 4 or len(team_B) > 4:
        termination_flag = True
        break

print(f'Team A - {(11 - len(team_A))}; Team B - {(11 - len(team_B))}')
if termination_flag:
    print('Game was terminated')
