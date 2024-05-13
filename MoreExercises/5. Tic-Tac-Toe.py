def check_win(_grid: list, player: str):
    for row in _grid:
        if row.count(player) == 3:
            return True

    for columns in range(3):
        column = [row[columns] for row in _grid]
        if column.count(player) == 3:
            return True

    primary_diagonal = [_grid[diagonal][diagonal] for diagonal in range(3)]
    if primary_diagonal.count(player) == 3:
        return True

    secondary_diagonal = [_grid[secondary_diagonal][len(_grid) - secondary_diagonal - 1] for secondary_diagonal
                          in range(3)]
    if secondary_diagonal.count(player) == 3:
        return True


grid: list = []

for i in range(3):
    grid.append(str.split(input()))

if check_win(grid, '1'):
    print('First player won')
elif check_win(grid, '2'):
    print('Second player won')
else:
    print('Draw!')
