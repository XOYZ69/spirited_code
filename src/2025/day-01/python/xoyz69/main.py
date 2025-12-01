dial = [x for x in range(100)]


def part01():
    print("2025 - Day 01 - part 01")

    dial_pointer = 50
    score = 0

    with open("input", "r") as input_file:
        operations = input_file.readlines()

    print(len(operations))

    for op in operations:
        if op.startswith("L"):
            direction = 1
        elif op.startswith("R"):
            direction = -1
        else:
            direction = 1
            print(f"Line could not be handled: [{op}]")

        steps = int(op[1:])

        dial_pointer = (dial_pointer - (steps * direction)) % len(dial)

        if dial_pointer == 0:
            score += 1

    print(f"Score: {score}")


if __name__ == "__main__":
    part01()
