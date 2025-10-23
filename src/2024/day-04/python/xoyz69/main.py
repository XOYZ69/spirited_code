import re

def part_1(lines):
    total = 0

    for y, line in enumerate(lines):
        # find horizontals
        total += len(re.findall('XMAS', line))
        total += len(re.findall('SAMX', line))

        for x in range(len(line)):
            try:
                # Vertical Down
                cache = ''.join(lines[y + n][x] for n in range(0, 4))
                if cache == 'XMAS' or cache == 'SAMX':
                    total += 1
            except Exception:
                pass

            try:
                # Dia Right Down
                cache = ''.join(lines[y + n][x + n] for n in range(0, 4))
                if cache == 'XMAS' or cache == 'SAMX':
                    total += 1
            except Exception:
                pass

            try:
                # Dia Left Down
                cache = ''.join(lines[y + n][x - n] for n in range(0, 4))
                if cache == 'XMAS' or cache == 'SAMX':
                    total += 1
            except Exception:
                pass


    print('Part 1 total:', total)

def part_2(lines):
    total = 0

    for y, line in enumerate(lines):
        line = line.strip()

        for x in range(len(line)):
            first_part = False
            second_part = False
            try:
                # Dia Right Down
                cache = lines[y - 1][x - 1] + lines[y][x] + lines[y + 1][x + 1]
                if cache == 'MAS' or cache == 'SAM':
                    first_part = True
            except Exception:
                pass

            try:
                # Dia Left Down
                cache = lines[y - 1][x + 1] + lines[y][x] + lines[y + 1][x - 1]
                if cache == 'MAS' or cache == 'SAM':
                    second_part = True
            except Exception:
                pass

            if first_part and second_part and y > 0:
                total += 1


    print('Part 2 total:', total)

def main():
    with open('../../.input', 'r', encoding = 'utf-8') as reader:
        lines = reader.readlines()

    part_1(lines)
    part_2(lines)

if __name__ == '__main__':
    main()
