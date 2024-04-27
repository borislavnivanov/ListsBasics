def put_out_fire(_water_used, _water) -> int or ValueError:
    if _water >= _water_used:
        _water -= _water_used
        return _water
    else:
        raise ValueError


def get_effort(_value: int) -> float:
    _effort = _value * 0.25
    return _effort


def check_fire_range(_type: str, _value: int) -> bool:
    if 0 < _value <= 50 and _type == 'Low':
        return True
    elif 50 < _value <= 80 and _type == 'Medium':
        return True
    elif 80 < _value <= 125 and _type == 'High':
        return True
    else:
        return False


def main():
    fires: list = str.split(input(), '#')
    water: int = int(input())
    effort: float = 0.00
    total_fires: int = 0

    print('Cells:')

    for fire in fires:
        fire_type, _cell_value = str.split(fire, ' = ')
        cell_value = int(_cell_value)

        if check_fire_range(fire_type, cell_value):
            try:
                water = put_out_fire(cell_value, water)
            except ValueError:
                continue
            else:
                effort += get_effort(cell_value)
                total_fires += cell_value
                print(f'- {cell_value}')

    print(f'Effort: {effort:.2f}\nTotal Fire: {total_fires}')


if __name__ == '__main__':
    main()
