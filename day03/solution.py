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

def create_grid(data):
    grid = []
    for line in data:
        grid.append([*line])
    return grid

def get_numbers_from_line(line):
    numbers = {}
    positions = []
    for match in re.finditer(r'[0-9]+',line):
        positions.append(match.span())
        if match.group() in numbers:                                # number can appear several times per row
            numbers[match.group()].append(match.span())             # append all appearances to list
        else:
            numbers[match.group()] = [match.span()]                 # set initial list with first appearance in row
    return numbers

def part1(data):
    sum = 0
    grid = create_grid(data)

    for row, line in enumerate(data):
        numbers = get_numbers_from_line(line)

        for n, positions in numbers.items():
            for position in positions:
                for col in range(position[0], position[1]):         # loop over each digit
                    if check_adjacent(grid, row, col):
                        sum += int(n)
                        break                                       # it's enough when first adjacent is found
    return sum

def part2(data):
    sum = 0
    grid = create_grid(data)
    gears = {}

    for row, line in enumerate(data):
        numbers = get_numbers_from_line(line)

        for n, positions in numbers.items():
            for position in positions:
                for col in range(position[0], position[1]):         # loop over each digit
                    gear_pos = check_gear(grid, row, col)
                    if gear_pos:
                        if gear_pos in gears:                       # check if position of gear is already in dict
                            sum += gears[gear_pos] * int(n)         # add to sum
                        else:
                            gears[gear_pos] = int(n)                # if not yet in dict, add
                        break                                       # it's enough when first gear is found
    return sum

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))