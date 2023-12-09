import re

TEST_CASE = """Time:      7  15   30
Distance:  9  40  200"""

def ways_beat_count(min_time: int, max_time: int, total_time: int, distance: int) -> int:
    mid = (max_time + min_time)//2
    d = mid * (total_time - mid)
    if min_time >= max_time:
        max_beat_time = mid if d > distance else mid+1
        return ((total_time + 1)//2 - max_beat_time) * 2 + 1-total_time % 2
    if d > distance:
        return ways_beat_count(min_time, mid - 1, total_time, distance)
    else:
        return ways_beat_count(mid + 1, max_time, total_time, distance)

def total_ways_beat(values: list) -> int:
    prod = 1
    nb_race = len(values)//2
    for i in range(nb_race):
        time = values[i]
        distance = values[i+nb_race]
        prod *= ways_beat_count(0, time, time, distance)
    return prod

def parse_races(races_data: str) -> list[int]:
    return [int(v) for v in re.findall(r'\d+', races_data)]

def parse_race(races_data: str) -> list[int]:
    return [int(''.join(re.findall(r'\d+', d))) for d in races_data.split("\n")]

with open('./2023/Day 6/input.txt', 'r') as f:
    input = f.read()
    assert(total_ways_beat(parse_races(TEST_CASE)) == 288)
    assert(total_ways_beat(parse_race(TEST_CASE)) == 71503)
    print("Part 1: " + str(total_ways_beat(parse_races(input))))
    print("Part 2: " + str(total_ways_beat(parse_race(input))))