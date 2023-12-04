import re
import numpy as np

TEST_CASE = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
MAX_BAG_CONTENT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def part_one(l: str) -> int:
    # extract
    game_id, grabed_cubes = l.split(":")

    # parse
    game_id = int(game_id[4:])
    grabed_cubes = re.findall(r'(\d* red)|(\d* green)|(\d* blue)', grabed_cubes)
    grabed_cubes = [tuple(''.join(t).split(" ")) for t in grabed_cubes]

    return 0 if any(int(n) > MAX_BAG_CONTENT[c] for n,c in grabed_cubes) else game_id

def part_two(l: str) -> int:
    grabed_cubes = re.findall(r'(\d* red)|(\d* green)|(\d* blue)', l)
    grabed_cubes = [tuple(''.join(t).split(" ")) for t in grabed_cubes]

    max_found_cubes = {"red": 0, "green": 0, "blue": 0}
    for n, c in grabed_cubes:
        max_found_cubes[c] = max(int(n), max_found_cubes[c])
    
    return np.prod(list(max_found_cubes.values()))

with open('d:/Programming/Misc/AdventOfCode/2023/Day 2/input.txt', 'r') as f:
    input = f.readlines()
    print("Part 1: " + str(sum([part_one(l) for l in input])))
    print("Part 2: " + str(sum([part_two(l) for l in input])))
