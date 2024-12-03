import re

mul_pattern = r'mul\(\d+,\d+\)'
sequence_pattern = r'mul\(\d+,\d+\)|don\'t\(\)|do\(\)'

def compute_uncorrupted_instruction(memory: str):
    mul_token = re.findall(mul_pattern, memory)
    acc = 0
    for token in mul_token:
        left, right = [int(number) for number in token[4:-1].split(',')]
        acc += left * right
    return acc

def compute_uncorrupted_instruction_sequence(memory: str):
    tokens = re.findall(sequence_pattern, memory)
    do_mul = True
    acc = 0
    for token in tokens:
        match token:
            case 'don\'t()':
                do_mul = False
            case 'do()':
                do_mul = True
            case _:
                if do_mul:
                    left, right = [int(number) for number in token[4:-1].split(',')]
                    acc += left * right
    return acc

with open('input.txt', 'r') as input:
    data = input.read()
    print(compute_uncorrupted_instruction(data))
    print(compute_uncorrupted_instruction_sequence(data))