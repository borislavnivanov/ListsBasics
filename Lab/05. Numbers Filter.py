n = int(input())

storage = []

for _ in range(n):
    storage.append(int(input()))

apply_filter = input()
result = []

if apply_filter == 'negative':
    for number in storage:
        if number < 0:
            result.append(number)
elif apply_filter == 'positive':
    for number in storage:
        if number >= 0:
            result.append(number)
elif apply_filter == 'odd':
    for number in storage:
        if number % 2 != 0:
            result.append(number)
elif apply_filter == 'even':
    for number in storage:
        if number % 2 == 0:
            result.append(number)

print(result)
