soldiers = str.split(input(), ' ')
roulette = int(input())
index = 0
counter = 0
homicides_indexes = []

while len(soldiers) > 0:
    counter += 1

    if counter % roulette == 0:
        homicides_indexes.append(soldiers.pop(index))
    else:
        index += 1

    if index >= len(soldiers):
        index = 0

print(str(homicides_indexes).replace('\'','').replace(' ', ''))
