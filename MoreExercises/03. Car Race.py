times = str.split(input())


def calculate_score(position: str) -> float:
    result = 0.00
    if position == 'left':
        for i in range(len(times) // 2):
            if times[i] == '0':
                result *= 0.8
            else:
                result += float(times[i])
    else:
        if position == 'right':
            for i in range(len(times) - 1, len(times) // 2, -1):
                if times[i] == '0':
                    result *= 0.8
                else:
                    result += float(times[i])
    return result


score_left = calculate_score('left')
score_right = calculate_score('right')

if score_left < score_right:
    print(f'The winner is left with total time: {score_left:.1f}')
else:
    print(f'The winner is right with total time: {score_right:.1f}')
