FIVE_KIND = 7
FOUR_KIND = 6
FULL_HOUSE = 5
THREE_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

TEST_CASE = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

def get_hand_type(cards: list, has_joker: bool) -> int:
    unique_cards_dict: dict = {}
    joker_count = 0
    for c in cards:
        if has_joker and c == 0:
            joker_count += 1
        elif unique_cards_dict.get(c):
            unique_cards_dict[c] += 1
        else:
            unique_cards_dict[c] = 1
    
    if joker_count == 5:
        return FIVE_KIND

    max_value_index = list(unique_cards_dict.values()).index(max(unique_cards_dict.values()))
    unique_cards_dict[list(unique_cards_dict.keys())[max_value_index]] += joker_count

    match len(unique_cards_dict.keys()):
        case 1 : return FIVE_KIND
        case 2:
            if max(unique_cards_dict.values()) == 4:
                return FOUR_KIND
            return FULL_HOUSE
        case 3: 
            if max(unique_cards_dict.values()) == 3:
                return THREE_KIND
            return TWO_PAIR
        case 4: return ONE_PAIR
        case _: return HIGH_CARD

def parse_cards(cards: str, has_joker: bool) -> list:
    parsed_cards = []

    for c in cards:
        match c:
            case 'A': parsed_cards.append(14)
            case 'K': parsed_cards.append(13)
            case 'Q': parsed_cards.append(12)
            case 'J': parsed_cards.append(0) if has_joker else parsed_cards.append(11)
            case 'T': parsed_cards.append(10)
            case _ : parsed_cards.append(int(c))

    return parsed_cards

def parse_hands(hands: str, has_joker: bool) -> list:
    parsed_hands = []

    for hand in hands.split('\n'):
        cards = parse_cards(hand[:5], has_joker)
        bid = int(hand[5:])
        parsed_hands.append((cards, get_hand_type(cards, has_joker), bid))
    return parsed_hands

def get_total_winnings(input: str, has_joker: bool) -> int:
    hands = parse_hands(input, has_joker)
    hands.sort(key=lambda a: (a[1], a[0][0], a[0][1], a[0][2], a[0][3], a[0][4]))
    return sum([hand[2] * (i+1) for i, hand in enumerate(hands)])

with open('./2023/Day 7/input.txt', 'r') as f:
    input = f.read()
    assert(get_total_winnings(TEST_CASE, False) == 6440)
    assert(get_total_winnings(TEST_CASE, True) == 5905)
    print("Part 1: " + str(get_total_winnings(input, False)))
    print("Part 2: " + str(get_total_winnings(input, True)))