import os

def solve(time, dist):
    res = 0
    for v in range(time):
        dist_traveled = 0
        if v == 0:
            continue
        
        time_left = time - v
        
        while (time_left > 0):
            dist_traveled += v

            if dist_traveled > dist:
                res += 1
                break
            
            time_left -= 1
    return res
            
def part1(times, dists):
    prod = 1
    for i in range(len(times)):
        prod *= solve(times[i], dists[i])
    return prod

def part2(times, dists):
    pass

if __name__ == "__main__":
    with open(os.path.dirname(os.path.realpath(__file__)) + '\\data.txt') as f:
        data = f.read().splitlines()

    times = [int(i.strip()) for i in data[0].split(':')[-1].split()]
    dists = [int(i.strip()) for i in data[1].split(':')[-1].split()]

    print(part1(times, dists))
    print(part2(times, dists))