import re
import numpy as np

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
    print(sum([part_two(l) for l in f.readlines()]))
