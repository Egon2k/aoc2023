import os

def extract_data(data):
    maps = {}
    seeds = [int(x.strip()) for x in data[0].split(':')[-1].split()]

    for i, line in enumerate(data):
        if i == 0 or line == "":
            continue

        if ":" in line:
            current = line[:-1]
            continue
        else:
            if current not in maps:
                maps[current] = [[int(x.strip()) for x in line.split()]]
            else:
                maps[current].append([int(x.strip()) for x in line.split()])
    return seeds, maps

def part1(data):
    seeds, maps = extract_data(data)
    for _, map in maps.items():
        for i, seed in enumerate(seeds):
            for rule in map:
                dest, src, len = rule
                if src <= seed < (src + len):
                    seeds[i] = dest + (seed - src)
    return min(seeds)   


def part2(data):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    print(part1(data))
    print(part2(data))