text = str.split(input(), ', ')

numbers: list = []
zeros: list = []

for char in text:
    if char != '0':
        numbers.append(int(char))
    else:
        zeros.append(int(char))

for zero in zeros:
    numbers.append(int(zero))
print(numbers)
