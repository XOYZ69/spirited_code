import re

def part_1(lines):
    total = 0
    for line in lines:
        matches = re.findall(r'mul\((0|[1-9][0-9]*),(0|[1-9][0-9]*)\)', line)

        for match in matches:
            total += int(match[0]) * int(match[1])

    print('Total part 1:', total)

def part_2(lines):
    total = 0
    last = 'do'
    for line in lines:
        for match in re.finditer(r'mul\((0|[1-9][0-9]*),(0|[1-9][0-9]*)\)|do\(\)|don\'t\(\)', line):
            if 'do()' in match.group():
                last = 'do'
                continue
            elif 'don\'t()' in match.group():
                last = 'dont'
                continue

            if last == 'do':
                cache = match.group().split(',')
                total += int(cache[0].split('(')[1]) * int(cache[1].replace(')', ''))

    print('Total part 2:', total)

def main():
    with open('../../.input', 'r', encoding='utf-8') as input_read:
        lines = input_read.readlines()

    part_1(lines)
    part_2(lines)

if __name__ == '__main__':
    main()
