deck = str.split(input(), ' ')
shuffles = int(input())
mid_deck = int(len(deck) / 2)


def shifter(_deck: list) -> list:
    start = _deck
    end: list = []
    for (a, b) in zip(start[0:mid_deck], start[mid_deck:len(start)]):
        end.append(a)
        end.append(b)

    return end


for i in range(shuffles):
    deck = shifter(deck)

print(deck)
