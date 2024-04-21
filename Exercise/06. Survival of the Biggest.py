numbers = str.split(input(), ' ')
int_to_remove = int(input())

sorted_list = []
for number in numbers:
    sorted_list.append(int(number))
sorted_list.sort()

for i in range(int_to_remove):
    g = sorted_list[i]
    numbers.remove(str(g))

for i in range(len(numbers)):
    print(f'{numbers[i]}', end='')
    if i != len(numbers) - 1:
        print(f', ', end='')
