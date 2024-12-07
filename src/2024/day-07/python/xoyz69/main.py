def part_1(lines):
    total = 0
    for line in lines:
        cache_line = line.replace('\n', '').split(': ')

        cache_target = int(cache_line[0])
        cache_parts = [int(x) for x in cache_line[1].split(' ')]

        counter = 0

        is_valid = False
        cache_result = 0

        while len(bin(counter)[2:]) < len(cache_parts) and not is_valid:

            cache_result = 0

            cc = f'0{bin(counter)[2:]:0>{len(cache_parts) - 1}}'
            for part_id in range(len(cache_parts)):

                if part_id <= len(cc) - 1 and cc[part_id] == '0':
                    cache_result += cache_parts[part_id]
                else:
                    cache_result *= cache_parts[part_id]

            is_valid = cache_result == cache_target
            counter += 1

        if is_valid:
            total += cache_result
            print(cache_target, cache_parts, cache_result, total)


    print('Part 1 total:', total)

def main():
    file = 'test_input'
    file = '../../.input'

    with open(file, 'r', encoding='utf-8') as reader:
        lines_read = reader.readlines()

    part_1(lines_read)

if __name__ == '__main__':
    main()
