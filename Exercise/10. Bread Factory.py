event_log: list = str.split(input(), '|')
energy: int = 100
coins: int = 100


def rest_event(_energy: int) -> int:
    new_energy = energy + _energy
    if new_energy > 100:
        new_energy = 100
    print(f'You gained {new_energy - energy} energy.\nCurrent energy: {new_energy}.')
    return new_energy


def order_event(_coins: int) -> int:
    if energy >= 30:
        globals().update(energy=energy - 30)
        print(f'You earned {_coins} coins.')
        new_coins = coins + _coins
        return new_coins
    else:
        print(f'You had to rest!')
        globals().update(energy=energy + 50)
        return coins


def ingredient_purchase(_ingredient: str, _price: int) -> Exception or None:
    if coins >= _price:
        globals().update(coins=coins - _price)
        print(f'You bought {_ingredient}.')
    else:
        print(f'Closed! Cannot afford {_ingredient}.')
        raise ValueError


def dispatch(_event: str, _number: int):
    if _event == 'rest':
        globals().update(energy=rest_event(_number))
        return 0
    elif _event == 'order':
        globals().update(coins=order_event(_number))
        return 0
    else:
        try:
            ingredient_purchase(_event, _number)
        except ValueError:
            return 1


for event in event_log:
    event_type, number = str.split(event, '-')
    value: int = int(number)
    status = dispatch(event_type, value)
    if status == 1:
        break
else:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
