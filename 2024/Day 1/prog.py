def compute_distance(left: list, right: list):
    left.sort()
    right.sort()
    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)
    return distance

def compute_similarity_score(left: list, right: list):
    left.sort()
    right.sort()
    similarity = 0
    i = 0
    for l in left:
        s = 0
        while i < len(right) and right[i] <= l:
            if right[i] == l:
                s += 1
            i += 1
        similarity += s * l
    return similarity

with open('./2024/Day 1/input.txt', 'r') as input:
    left = []
    right = []
    for line in input.readlines():
        l, r = line.strip().split('   ')
        left.append(int(l))
        right.append(int(r))
    # print(compute_distance(left, right))
    print(compute_similarity_score(left, right))
