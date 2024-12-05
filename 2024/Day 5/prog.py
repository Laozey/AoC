from typing import Union

def swap(a: str, b: str, l: list) -> list:
    i = l.index(a)
    j = l.index(b)
    l[i], l[j] = l[j], l[i]
    return l

# IMPROVE: May be done better
def reorder_pages(rules: dict, pages: list) -> list:
    i = 0
    while i < len(pages):
        p = pages[i]
        left = pages[:i]
        for l in left:
            if l in rules[p]:
                i = pages.index(l)
                swap(l, p, pages)
                break
        right = pages[i+1:]
        for r in right:
            if p in rules[r]:
                i -= 1
                swap(r, p, pages)
                break
        i+=1
    return pages

def sum_middle_pages(rules: dict, data: list) -> int:
    acc = 0
    reordered_acc = 0
    for pages in data:
        if are_pages_ordered(rules, pages):
            acc += int(pages[len(pages)//2])
        else:
            reordered_pages = reorder_pages(rules, pages)
            reordered_acc += int(reordered_pages[len(reordered_pages)//2])
    return acc, reordered_acc

def are_pages_ordered(rules: dict, pages: list):
    for i, p in enumerate(pages):
        left = pages[:i]
        if any([l in rules[p] for l in left]):
            return False
        right = pages[i+1:]
        if any([p in rules[r] for r in right]):
            return False
    return True

def read_input(input: str) -> Union[dict, list]:
    rules_raw, data_raw = input.split('\n\n')
    rules = {}
    for r in rules_raw.split('\n'):
        key, value = r.split('|')
        if rules.get(key) != None:
           rules[key].append(value)
        else:
           rules[key] = [value]
    data = []
    for d in data_raw.split('\n'):
        data.append(d.split(','))
    return rules, data

with open('./2024/Day 5/input.txt', 'r') as input:
    rules, data = read_input(input.read())
    print(sum_middle_pages(rules, data))
    