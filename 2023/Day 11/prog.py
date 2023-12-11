TEST_CASE = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# 0 cost up/down , 1 cost left/right
SPACE_COST = [[], []]
GALAXY_MAP = []

def get_shortest_path_length(start: tuple, end: tuple):
    x_cost = 0
    y_cost = 0
    for i in range(min(start[0], end[0]), max(start[0], end[0])):
        x_cost += SPACE_COST[0][i]
    for i in range(min(start[1], end[1]), max(start[1], end[1])):
        y_cost += SPACE_COST[1][i]
    length = x_cost + y_cost
    # print("(" + str(start[0])+ ", " + str(start[1]) + ") - (" + str(end[0])+ ", " + str(end[1]) + "): " + str(length))
    return length

def parse_galaxy(galaxy: str, expansion_cost: int) -> None:
    galaxy = galaxy.split('\n')

    SPACE_COST[0].clear()
    SPACE_COST[1].clear()
    GALAXY_MAP.clear()
    for i in range(len(galaxy)):
        SPACE_COST[0].append(expansion_cost if all(space == '.' for space in galaxy[i]) else 1)
    
    for j in range(len(galaxy[0])):
        SPACE_COST[1].append(expansion_cost if all(galaxy[i][j] == '.' for i in range(len(galaxy))) else 1)

    for i, g_line in enumerate(galaxy):
        for j, space in enumerate(g_line):
            if space == '#':
                GALAXY_MAP.append((i, j))

def total_path_length() -> None:
    pairs_path_length = []
    for i, s_galaxy in enumerate(GALAXY_MAP):
        for e_galaxy in GALAXY_MAP[i:]:
            pairs_path_length.append(get_shortest_path_length(s_galaxy, e_galaxy))
    res= sum(pairs_path_length)
    return res

with open('./2023/Day 11/input.txt', 'r') as f:
    input = f.read()
    parse_galaxy(TEST_CASE, 2)
    assert(total_path_length() == 374)
    parse_galaxy(TEST_CASE, 10)
    assert(total_path_length() == 1030)
    parse_galaxy(TEST_CASE, 100)
    assert(total_path_length() == 8410)
    parse_galaxy(input, 1)
    print("Part 1: " + str(total_path_length()))
    parse_galaxy(input, 1000000)
    print("Part 2: " + str(total_path_length()))