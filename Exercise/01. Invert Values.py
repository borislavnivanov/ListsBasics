text = input()
values: list = text.split(' ')

for i in range(len(values)):
    _change = int(values[i])
    if _change < 0:
        _change = abs(_change)
    else:
        _change = -abs(_change)
    values[i] = _change

print(values)
