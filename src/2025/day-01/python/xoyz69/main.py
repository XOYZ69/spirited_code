dial = [x for x in range(100)]


def part01():
    print("2025 - Day 01 - part 01")

    dial_pointer = 50
    score = 0

    with open("input", "r") as input_file:
        operations = input_file.readlines()

    print("Input length", len(operations))

    for op in operations:
        direction = 1 if op.startswith("L") else -1

        steps = int(op[1:])

        dial_pointer = (dial_pointer - (steps * direction)) % len(dial)

        if dial_pointer == 0:
            score += 1

    print(f"Score: {score}")


def part02():
    print("2025 - Day 01 - part 02")

    dial_pointer = 50
    score = 0

    with open("input", "r") as input_file:
        operations = input_file.readlines()

    print("Input length", len(operations))

    for op in operations:
        direction = 1 if op.startswith("L") else -1

        steps = int(op[1:])

        dial_pointer_prev = dial_pointer
        turn = dial_pointer - (steps * direction)
        dial_pointer = turn % len(dial)

        score += int(abs(turn) / len(dial))

        score += 1 if turn < 0 else 0

    print(f"Score: {score}")


if __name__ == "__main__":
    print("--------------")
    part01()
    print("--------------")
    part02()
