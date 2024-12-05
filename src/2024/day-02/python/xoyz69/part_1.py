# load and prepare puzzle input
with open('../../.input', 'r', encoding='utf-8') as reader:
    raw_lines = reader.readlines()

def valid_report(level):
    level = level.replace('\n', '')

    levels = [int(x) for x in level.split(' ')]

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])

        if diff < 1 or diff > 3:
            return False

    last_number = levels[0]
    for i in range(1, len(levels)):
        if levels[0] < levels[1]:
            if levels[i] < last_number:
                print(level)
                return False
            last_number = levels[i]
        else:
            if levels[i] > last_number:
                print(level)
                return False
            last_number = levels[i]

    return True

valid_reports = sum(valid_report(x) for x in raw_lines)

print(f'Valid reports: {valid_reports}')
