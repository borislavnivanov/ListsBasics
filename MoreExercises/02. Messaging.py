numbers = str.split(input())
text_inp = input()
text = []
sum_numbers = []
decoded = ''

for char in text_inp:
    text.append(char)

for number in numbers:
    a = 0
    for char in number:
        a += int(char)
    sum_numbers.append(a)

for number in sum_numbers:
    a = number % len(text)
    decoded += text[a]
    text.pop(a)

print(decoded)
