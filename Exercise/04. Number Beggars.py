coins: list = str.split(input(), ', ')
for i in range(len(coins)):
    coins[i] = int(coins[i])
beggars = int(input())
beggars_turnout = [0] * beggars
pass_count: int = 0

while len(coins) > 0:
    beggars_turnout[pass_count] += coins[0]
    del coins[0]
    pass_count += 1
    if pass_count >= beggars:
        pass_count = 0

print(beggars_turnout)
