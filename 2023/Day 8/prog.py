TEST_CASE = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST_CASE_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

TEST_CASE_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

NETWORK_MAP = {}

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_list(steps: list[int]):
    lcm_result = 1
    for s in steps:
        lcm_result = (lcm_result * s) // gcd(lcm_result, s)
    return lcm_result

def is_arrived(nodes: list[str], ends: list[str]):
    return all(n in ends for n in nodes)

def get_nb_step(network: tuple) -> int:
    sequence = network[0]
    nodes = network[1]
    steps = [0 for _ in nodes]
    ends = network[2]
    s_i = 0
    s_l = len(sequence)
    for i in range(len(nodes)):
        while(not nodes[i] in ends):
            nodes[i] = NETWORK_MAP[nodes[i]][sequence[s_i] == 'R']
            s_i = (s_i + 1) % s_l
            steps[i] += 1
    return lcm_list(steps)

def fill_network_data(instructions: list) -> None:
    for i in instructions:
        NETWORK_MAP[i[:3]] = (i[7:10], i[12:15])

def parse_network(document: str) -> (str, str, str):
    network = document.split('\n')
    fill_network_data(network[2:])
    return network[0], ['A'*3], ['Z'*3]

def parse_network_all(document: str) -> (str, list, list):
    network = document.split('\n')
    instructions = network[2:]
    fill_network_data(instructions)
    start = []
    end = []
    for i in instructions:
        node = i[:3]
        if node.endswith('A'):
            start.append(node)
        elif node.endswith('Z'):
            end.append(node)
    return network[0], start, end

with open('./2023/Day 8/input.txt', 'r') as f:
    input = f.read()
    assert(get_nb_step(parse_network(TEST_CASE)) == 2)
    assert(get_nb_step(parse_network(TEST_CASE_2)) == 6)
    assert(get_nb_step(parse_network_all(TEST_CASE_3)) == 6)
    print("Part 1: " + str(get_nb_step(parse_network(input))))
    print("Part 2: " + str(get_nb_step(parse_network_all(input))))