n = int(input())
word = input()

strings: list = []

for _ in range(n):
    strings.append(input())

print(strings)

for i in range(len(strings) - 1, - 1, - 1):
    entry = strings[i]
    if word not in entry:
        strings.remove(entry)

print(strings)
