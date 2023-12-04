import numpy as np

TEST_CASE = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]
SYMBOLS = ['*', '#', '%', '/', '=', '$', '+', '-', '@', '&']
CONVOLUTION_MATRIX = [
    (-1, -1), #7
    (-1,  0), #8
    (-1,  1), #9
    ( 0,  1), #6
    ( 1,  1), #3
    ( 1,  0), #2
    ( 1, -1), #1
    ( 0, -1), #4
]

def find_part_number(lines: list) -> list:
    total_sum = 0
    gear_ratio = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[i]) -1):
            if lines[i][j] in SYMBOLS:
                parts_number = convolution((i, j), lines)
                total_sum += sum(parts_number)
                if len(parts_number) == 2:
                    gear_ratio += np.prod(parts_number)
    return total_sum, gear_ratio

def convolution(index: tuple, lines: list) -> list:
    engine_parts = []
    for c in CONVOLUTION_MATRIX:
        i = index[0] + c[0]
        j = index[1] + c[1]
        if lines[i][j].isnumeric():
            engine_parts.append(extract_number(lines[i], j))
    return np.unique(engine_parts)

def extract_number(line: str, mid: int) -> int:
    n = len(line)
    number = line[mid]
    i = mid
    for _ in range(2):
        if i-1 < 0 or not line[i - 1].isnumeric():
            break
        else:
            i -= 1
            number = line[i] + number

    i = mid
    for _ in range(2):
        if i+1 >= n or not line[i + 1].isnumeric():
            break
        else:
            i += 1
            number += line[i]
    
    return int(number)

with open('./2023/Day 3/input.txt', 'r') as f:
    input = f.readlines()
    p1, p2 = find_part_number(input)
    print("Part 1: " + str(p1))
    print("Part 2: " + str(p2))