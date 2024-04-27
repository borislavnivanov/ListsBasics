def out_of_stock(item: str) -> None:
    for i in range(len(gifts)):
        if gifts[i] == item:
            required_on_index('None', i)


def required_on_index(item: str, _index: int) -> None:
    if 0 <= _index < len(gifts):
        gifts[_index] = item


def just_in_case(item: str) -> None:
    gifts[-1] = item


gifts: list = str.split(input())

while True:
    text = input()
    if text == 'No Money':
        break

    command: list = str.split(text)

    if command[0] == 'OutOfStock':
        out_of_stock(command[1])
    elif command[0] == 'Required':
        required_on_index(command[1], int(command[2]))
    elif command[0] == 'JustInCase':
        just_in_case(command[1])

for index in gifts:
    if index != 'None':
        print(f'{index} ', end='')
