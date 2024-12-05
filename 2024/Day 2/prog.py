def find_safe_reports(reports: list):
    safe_count = 0
    unsafe_reports = []
    for report in reports:
        if is_report_safe(report):
            safe_count += 1
        else:
            unsafe_reports.append(report)
    dampener_safe_count = 0
    for report in unsafe_reports:
        if is_unsafe_report_safe(report):
            dampener_safe_count += 1
    return safe_count, safe_count + dampener_safe_count

def is_report_safe(report: list) -> bool:
    prev = report[0]
    prev_sign = sign(report[1] - prev)
    for level in report[1:]:
        diff = level - prev
        new_sign = sign(diff)
        if not is_level_safe(diff, new_sign + prev_sign):
            return False
        prev = level
        prev_sign = new_sign
    return True

# Better solution but not from me
def is_safe(report):
    increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_unsafe_report_safe(unsafe_report: list) -> bool:
    prev = unsafe_report[0]
    prev_sign = sign(unsafe_report[1] - prev)
    i = 1
    while i < len(unsafe_report):
        level = unsafe_report[i]
        diff = level - prev
        new_sign = sign(diff)
        if not is_level_safe(diff, new_sign + prev_sign):
            a = unsafe_report[max(i-2,0):]
            b = unsafe_report[max(i-2,0):]
            if len(a) == 3:
                return True
            a.remove(level)
            b.remove(prev)
            return is_report_safe(a) or is_report_safe(b)
        prev = level
        prev_sign = new_sign
        i += 1
    return True

def is_level_safe(diff, sign) -> bool:
    return 0 < abs(diff) <= 3 and abs(sign) == 2

def sign(a):
    return (a > 0) - (a < 0)

with open('./2024/Day 2/input.txt', 'r') as input:
    reports = []
    for line in input.readlines():
        reports.append([int(level) for level in line.strip().split(' ')])
    print(find_safe_reports(reports))