import threading
from itertools import combinations, permutations

from tqdm import tqdm


def part01():
    print("Advent of Code 2025 - Day 03 Part 1")

    with open("input", "r") as file_input:
        lines = file_input.readlines()

    total_joltage = 0

    for line in lines:
        line = line.replace("\n", "")
        biggest = 0
        x, y = 0, 0
        for a in range(len(line) - 1):
            for b in range(len(line)):
                if a == b or b < a:
                    continue

                nr = int(f"{line[a]}{line[b]}")

                if nr > biggest:
                    biggest = nr
                    x, y = a, b

        print(f" -> Bank [{line}]: {biggest} | {x}/{y}")
        total_joltage += biggest

    print(f"Result: {total_joltage}")


def part02():
    print("Advent of Code 2025 - Day 03 Part 2")

    with open("input", "r") as file_input:
        lines = file_input.readlines()

    total_joltage = 0

    def is_order(a):
        sorte = sorted(a)
        for x in range(len(a)):
            if a[x] != sorte[x]:
                return False
        return True

    for line in tqdm(lines):
        line = line.replace("\n", "")
        biggest = 0

        high_by_order_old = sorted(
            [x for x in range(len(line))], key=lambda x: int(line[x]), reverse=True
        )

        indicell = [x for x in range(len(line))]

        # print(f"Bank [{line}] | {indicell}")

        for indicies in combinations(indicell, 12):
            if not is_order(indicies):
                continue

            current = int("".join([line[x] for x in indicies]))

            if current > biggest:
                biggest = current
                # print(f" - Found new biggest: {biggest}")

        # biggest = int("".join([str(high_by_order[x]) for x in range(12)]))

        print(f"\t Result: {biggest}")
        total_joltage += biggest

    print(f"Result: {total_joltage}")


if __name__ == "__main__":
    print("----------")
    part01()
    print("----------")
    part02()
