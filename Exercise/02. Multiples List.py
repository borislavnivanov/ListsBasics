factor = int(input())
count = int(input())
result: list = []

for i in range(1, count + 1):
    result.append(i * factor)

print(result)
