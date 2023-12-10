TEST_CASE = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def find_history_value(history_line: list[int], backward: bool) -> int:
    if all(n == 0 for n in history_line):
        return 0

    extrapolated_history = []
    for i in range(1, len(history_line)):
        extrapolated_history.append(history_line[i] - history_line[i-1])
    if backward:
        return history_line[0] - find_history_value(extrapolated_history, backward)
    return history_line[-1] + find_history_value(extrapolated_history, backward)
        

def total_report_values(report_lines: list, backward: bool) -> int:
    return sum(find_history_value(h_line, backward) for h_line in report_lines)

def parse_report(report: str):
    lines = []
    for l in report.split('\n'):
        lines.append([int(n) for n in l.split(' ')])
    return lines

with open('./2023/Day 9/input.txt', 'r') as f:
    input = f.read()
    assert(total_report_values(parse_report(TEST_CASE), False) == 114)
    assert(total_report_values(parse_report(TEST_CASE), True) == 2)
    print("Part 1: " + str(total_report_values(parse_report(input), False)))
    print("Part 2: " + str(total_report_values(parse_report(input), True)))