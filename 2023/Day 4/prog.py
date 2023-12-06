import re
import numpy as np

TEST_CASE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def get_winning_match(card: str) -> int:
    gotten, winning = card[9:].split('|')
    gotten = [int(e) for e in re.findall(r'\d+', gotten)]
    gotten.sort()
    winning = [int(e) for e in re.findall(r'\d+', winning)]
    winning.sort()

    i = 0
    j = 0
    w = 0
    while(i < len(gotten) and j < len(winning)):
        if gotten[i] == winning[j]:
            w += 1
        if gotten[i] > winning[j]:
            j += 1
        else:
            i += 1
    
    return w

def compute_cards_score(cards: list) -> int:
    sum = 0
    for c in cards:
        m = get_winning_match(c)
        sum += 2**(m-1) if m else 0
    return sum

def compute_cards_count(cards: list) -> int:
    cards_count = np.array([1] * len(cards))
    for i, c in enumerate(cards):
        for m in range(get_winning_match(c)):
            cards_count[i+1+m] += cards_count[i]
    return sum(cards_count)


with open('./2023/Day 4/input.txt', 'r') as f:
    cards = f.readlines()
    assert(compute_cards_score(TEST_CASE.split('\n')) == 13)
    assert(compute_cards_count(TEST_CASE.split('\n')) == 30)
    print("Part 1: " + str(compute_cards_score(cards)))
    print("Part 2: " + str(compute_cards_count(cards)))