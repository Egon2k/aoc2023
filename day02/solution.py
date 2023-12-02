import os

def part1(data):
    sum = 0
    for id, game in enumerate(data):
        possible = True
        set = game.split(";")
        for subset in set:
            for draw in subset.split(","):
                draw = draw.strip()
                number = int(draw.split()[0])
                color = draw.split()[1]
                if (color == 'red' and number > 12) or (color == 'green' and number > 13) or (color == 'blue' and number > 14):
                    possible = False
        if possible:
            sum += (id + 1)
    return sum            

def part2(data):
    sum = 0
    for game in data:
        reds = blues = greens = 0
        set = game.split(";")
        for subset in set:
            for draw in subset.split(","):
                draw = draw.strip()
                number = int(draw.split()[0])
                color = draw.split()[1]

                if color == 'red':
                    reds = max(reds, number)
                elif color == 'green':
                    greens = max(greens, number)
                elif color == 'blue':
                    blues = max(blues, number)
        sum += reds * blues * greens
    return sum 

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    for i in range(len(data)):  # cut off "Game <ID>"
        data[i] = data[i].split(":")[-1].strip()
    
    print(part1(data))
    print(part2(data))