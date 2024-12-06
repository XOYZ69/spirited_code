def part_1(order, numbers):
    correct_sequence = []
    for sequence in numbers:
        correctly_ordered = True
        for rule in order:
            # check if rule is in the sequence
            index_a, index_b = -1, -1
            for i in range(len(sequence)):
                if sequence[i] == rule[0]:
                    index_a = i
                if sequence[i] == rule[1]:
                    index_b = i

            # Skip if rule does not need to be applied
            if index_a == -1 or index_b == -1:
                continue

            # Check if rule is valid for this sequence
            if index_a > index_b:
                correctly_ordered = False

        if correctly_ordered:
            correct_sequence.append(sequence)

    total = 0
    for seq in correct_sequence:
        total += seq[int(len(seq) / 2)]

    print('Part 1:', total)



def part_2():
    pass

def main():
    with open('../../.input', 'r', encoding = 'utf-8') as reader:
        lines = reader.readlines()

    # preperation of arrays
    page_ordering = []
    page_numbers = []

    for line in lines:
        cline = line.replace('\n', '')
        if cline == '':
            page_ordering = page_numbers
            page_numbers = []
            continue
        page_numbers.append(cline)

    # Convert arrays to let them be more easily handled later
    for i in range(len(page_ordering)):
        cache = page_ordering[i].split('|')
        page_ordering[i] = [int(j) for j in cache]

    for i in range(len(page_numbers)):
        cache = page_numbers[i].split(',')
        page_numbers[i] = [int(j) for j in cache]

    # run the parts
    part_1(page_ordering, page_numbers)

if __name__ == '__main__':
    main()
