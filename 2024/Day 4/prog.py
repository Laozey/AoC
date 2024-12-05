DIRECTIONS = [
    [-1,  1],
    [ 0,  1],
    [ 1,  1],
    [ 1,  0],
]

def is_word_occurrence_in_dir(data, word, i, x, y, dx, dy):
    if i >= len(word):
        return True
    can_check = 0 <= x < len(data) and 0 <= y < len(data[0])
    if not can_check:
        return False
    if data[x][y] == word[i]:
        return is_word_occurrence_in_dir(data, word, i + 1, x + dx, y + dy, dx, dy)
    return False

def count_word_occurrence_around(data, word, x, y) -> int:
    acc = 0
    for dx, dy in DIRECTIONS:
        if is_word_occurrence_in_dir(data, word, 1, x + dx, y + dy, dx, dy):
            acc += 1
        if is_word_occurrence_in_dir(data, word, 1, x - dx, y - dy, -dx, -dy):
            acc += 1
    return acc

def count_xmas(data, width, height0) -> int:
    acc = 0
    for x in range(width):
        for y in range(height):
            if data[x][y] == 'X':
                acc += count_word_occurrence_around(data, 'XMAS', x, y)
    return acc

def is_word_occurrence_in_x(data, word, x, y):
    d1 = data[x-1][y-1]+data[x][y]+data[x+1][y+1]
    d2 = data[x-1][y+1]+data[x][y]+data[x+1][y-1]
    return (d1 == word or d1[::-1] == word) and (d2 == word or d2[::-1] == word)

def count_x_mas(data, width, height) -> int:
    acc = 0
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            if data[x][y] == 'A' and is_word_occurrence_in_x(data, 'MAS', x, y):
                acc += 1
    return acc

with open('./2024/Day 4/input.txt', 'r') as input:
    data = [line.strip() for line in input.readlines()]
    width, height = len(data), len(data[0])
    print(count_xmas(data, width, height))
    print(count_x_mas(data, width, height))