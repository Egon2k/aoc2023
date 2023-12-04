import os

def part1(data):
    sum = 0

    for card in data:
        winning_numbers = [int(i) for i in card.split('|')[0].split()]
        my_numbers = [int(i) for i in card.split('|')[1].split()]

        matches = len(set(winning_numbers) & set(my_numbers))
        if matches > 0:
            sum += 2**(matches-1)
    return sum


def part2(data):
    copies = {}
    
    for game_id, _ in enumerate(data):
        copies[game_id] = 1

    for game_id, card in enumerate(data):
        winning_numbers = [int(i) for i in card.split('|')[0].split()]
        my_numbers = [int(i) for i in card.split('|')[1].split()]
        
        matches = len(set(winning_numbers) & set(my_numbers))
    
        for match in range(matches):
            copies[game_id + match + 1] += copies[game_id]

    return sum(copies.values())

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    for i in range(len(data)):  # cut off "Card <ID>"
        data[i] = data[i].split(':')[-1].strip()

    print(part1(data))
    print(part2(data))