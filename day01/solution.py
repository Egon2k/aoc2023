def part1(data):
    sum = 0
    for line in data:
        digits = []
        for x in line:
            if x.isdigit():
                digits.append(x)
        sum += int(digits[0]) * 10 + int(digits[-1])
    return sum

def part2(data):
    pass

if __name__ == "__main__":
    with open('day01/data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))