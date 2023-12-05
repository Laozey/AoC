TEST_CASE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

seeds = []

def parse_almanac(almanac: str) -> int:
    pages = almanac.split("\n\n")
    seeds = extract_seeds(pages[0])
    for i in range(1, len(pages)):
        for j, s in enumerate(seeds):
            for r in pages[i].split("\n")[1:]:
                dest, source, length = [int(e) for e in r.split(' ')]
                diff = source - s
                abs_diff = abs(diff)
                if diff <= 0 and abs_diff < length:
                    seeds[j] = dest + abs_diff
    return min(seeds)

def parse_almanac_range(almanac: str) -> int:
    pages = almanac.split("\n\n")
    seeds = extract_seeds_range(pages[0])
    return min([process_page(s, pages, 1) for s in seeds])

def process_page(range_seed: tuple, pages: list[str], i: int):
    if i >= len(pages):
        return range_seed[0]

    to_process = [range_seed]
    range_seeds = []
    for r in pages[i].split("\n")[1:]:
        dest, source, length = [int(e) for e in r.split(' ')]
        source_range = (source, source + length-1)

        if len(to_process) == 0:
            break

        rs = to_process[0]
        intersection, left_over = intersect_range(rs, source_range)
        if intersection[0] > intersection[1]:
            continue
        to_process.pop()
        to_process.extend(left_over)
        new_rs_min = dest + abs(intersection[0] - source_range[0])
        new_rs_max = dest + abs(intersection[1] - source_range[0])
        range_seeds.append((new_rs_min, new_rs_max))

    range_seeds.extend(to_process)
    return min([process_page(r, pages, i+1) for r in range_seeds])

def intersect_range(a: tuple, b: tuple) -> tuple:
    intersect = (max(a[0], b[0]), min(a[1], b[1]))
    left_over = []
    if a[0] < b[0]:
        left_over.append((a[0], b[0] - 1))
    if a[1] > b[1]:
        left_over.append((b[1] + 1, a[1]))
    return intersect, left_over

def map_range(value: int, old_range: tuple, new_range: tuple) -> int:
    o_range = old_range[1] - old_range[0]
    n_range = new_range[1] - new_range[0]
    return ((value - old_range[0]) // o_range) * n_range + new_range[0] 

def extract_seeds(page: str) -> list[int]:
    return [int(e) for e in page[7:].split(' ')]

def extract_seeds_range(page: str) -> list[int]:
    numbers = [int(e) for e in page[7:].split(' ')]
    for i in range(0, len(numbers), 2):
        seeds.append((numbers[i], numbers[i] + numbers[i+1] - 1))
    return seeds

with open('./2023/Day 5/input.txt', 'r') as f:
    input = f.read()
    assert(parse_almanac(TEST_CASE) == 35)
    # assert(parse_almanac_range(TEST_CASE) == 46)
    print("Part 1: " + str(parse_almanac(input)))
    print("Part 2: " + str(parse_almanac_range(input)))