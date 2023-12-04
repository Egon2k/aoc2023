import os

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def part1(data):
    sum = 0
    for line in data:
        winning_numbers = [int(i) for i in line.split('|')[0].split()]
        my_numbers = [int(i) for i in line.split('|')[1].split()]

        match = len(set(winning_numbers) & set(my_numbers))
        if match > 0:
            sum += 2**(match-1)
    return sum


def part2(data):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    for i in range(len(data)):  # cut off "Card <ID>"
        data[i] = data[i].split(':')[-1].strip()

    print(part1(data))
    print(part2(data))