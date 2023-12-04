import re

numerics = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def calibration_value(s):
    l = (len(s), "")
    r = (-1, "")
    for n in numerics + numbers:
        idx = list(re.finditer(n, s))
        if len(idx) != 0:
            start = idx[0].start()
            end = idx[-1].start()
            if start < l[0]:
                l = (start, parse_to_int(s[start:start+len(n)]))
            if end > r[0]:
                r = (end, parse_to_int(s[end:end+len(n)]))
    
    return int(l[1]+r[1])

def parse_to_int(s):
    match s:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return s

with open('./2023/Day 1/input.txt', 'r') as f:
    sum = 0
    for l in f.readlines():
        sum += calibration_value(l)
    print(sum)