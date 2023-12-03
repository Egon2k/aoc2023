import os, re

def check_adjacent(grid, row, col):
    border_row = (0, len(grid))
    border_col = (0, len(grid[0]))
    for srow in [-1, 0 , 1]:
        for scol in [-1, 0 , 1]:
            if srow == 0 and scol == 0:
                continue
            new_row = row + srow
            new_col = col + scol
            
            if border_row[0] < (new_row) < border_row[1] and \
               border_col[0] < (new_col) < border_col[1]:
                if not(grid[new_row][new_col].isdigit() or \
                       grid[new_row][new_col] == '.'):
                    return True
    return False



def part1(data):
    sum = 0
    
    grid = []
    for line in data:
        grid.append([*line])

    for row, line in enumerate(data):
        numbers = {}
        for match in re.finditer(r'[0-9]+',line):
            if match.group() in numbers:
                print(match.group())
            numbers[match.group()] = match.span()

        for n, pos in numbers.items():
            for col in range(pos[0], pos[1]):
                if check_adjacent(grid, row, col):
                    sum += int(n)
                    break
    return sum
                    
def part2(data):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))