meerkat: list = []
for _ in range(3):
    meerkat.append(input())

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]

print(meerkat)
