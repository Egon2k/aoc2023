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

def check_gear(grid, row, col):
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
                if grid[new_row][new_col] == '*':
                    return (new_row, new_col)
    return None



def part1(data):
    sum = 0
    
    grid = []
    for line in data:
        grid.append([*line])

    for row, line in enumerate(data):
        numbers = {}
        positions = []
        for match in re.finditer(r'[0-9]+',line):
            positions.append(match.span())
            if match.group() in numbers: # number was already in that row, add a second position to dict
                numbers[match.group()].append(match.span())
            else:
                numbers[match.group()] = [match.span()]

        for n, positions in numbers.items():
            for position in positions:
                for col in range(position[0], position[1]):
                    if check_adjacent(grid, row, col):
                        sum += int(n)
                        break
    return sum
                    
def part2(data):
    sum = 0
    gears = {}

    grid = []
    for line in data:
        grid.append([*line])

    for row, line in enumerate(data):
        numbers = {}
        positions = []
        for match in re.finditer(r'[0-9]+',line):
            positions.append(match.span())
            if match.group() in numbers: # number was already in that row, add a second position to dict
                numbers[match.group()].append(match.span())
            else:
                numbers[match.group()] = [match.span()]

        for n, positions in numbers.items():
            for position in positions:
                for col in range(position[0], position[1]):
                    gear_pos = check_gear(grid, row, col)
                    if gear_pos:
                        if gear_pos in gears:
                            sum += gears[gear_pos] * int(n)
                        else:
                            gears[gear_pos] = int(n)
                        break
    return sum

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))