# load and prepare puzzle input
with open('../../.input', 'r', encoding='utf-8') as reader:
    raw_lines = reader.readlines()

def valid_report(level):
    print('----------', level)

    valid = True

    for j in range(len(level) - 1):
        diff = abs(level[j] - level[j + 1])
        print(diff, level[j], j)

        if diff < 1 or diff > 3:
            valid = False

    if not counting_down(level) and not counting_up(level):
        valid = False

    # last_number = levels[0]
    # for i in range(1, len(levels)):
    #     if levels[0] < levels[1]:
    #         if levels[i] < last_number:
    #             return False
    #         last_number = levels[i]
    #     else:
    #         if levels[i] > last_number:
    #             return False
    #         last_number = levels[i]

    return valid

def counting_down(sequence):
    for k in range(len(sequence) - 1):
        if sequence[k] > sequence[k + 1]:
            return False

    return True

def counting_up(sequence):
    for k in range(len(sequence) - 1):
        if sequence[k] < sequence[k + 1]:
            return False

    return True

valid_reports = 0

for i, report in enumerate(raw_lines):

    level = report.replace('\n', '')

    levels = [int(x) for x in level.split(' ')]

    valid = valid_report(levels)

    if not valid:
        for i in range(len(levels)):
            level_cache = levels.copy()
            level_cache.pop(i)
            valid = valid_report(level_cache)
            print(level_cache, valid)
            if valid:
                break

    if valid:
        valid_reports += 1

print(f'Valid reports: {valid_reports}')
