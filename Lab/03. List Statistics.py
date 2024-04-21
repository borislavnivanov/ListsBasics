n = int(input())

positive: list = []
negative: list = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

sum_negatives = 0
for number in negative:
    sum_negatives += number

print(f'{positive}\n{negative}')
print(f'Count of positives: {len(positive)}\nSum of negatives: {sum_negatives}') #sum(negatives)
