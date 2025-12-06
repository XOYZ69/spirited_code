import time

from tqdm import tqdm


def part01():
    print("Advent of Code 2025 - Day 05 Part 01")

    with open("input", "r") as file_input:
        combined_input = file_input.read()
        fresh_ranges, ingridients = [
            x.strip().split("\n") for x in combined_input.split("\n\n")
        ]

    pre_fresh_list = [nr for nr in [x.split("-") for x in fresh_ranges]]

    fresh_list = []

    for ran in pre_fresh_list:
        fresh_list.append([int(ran[0]), int(ran[1])])

    yes_fresh = 0

    for i in ingridients:
        i = int(i)

        for j in fresh_list:
            if i >= j[0] and i <= j[1]:
                yes_fresh += 1
                break

    print(f"Result: {yes_fresh}")


def part02():
    print("Advent of Code 2025 - Day 05 Part 02")

    with open("input", "r") as file_input:
        combined_input = file_input.read()
        fresh_ranges, ingridients = [
            x.strip().split("\n") for x in combined_input.split("\n\n")
        ]

    pre_fresh_list = [[int(n) for n in x.split("-")] for x in fresh_ranges]
    fresh: list[list[int]] = []

    range_start = []
    range_end = []

    def if_in_get_index(x):
        for i in range(len(fresh)):
            compare = x >= fresh[i][0] and x <= fresh[i][1]
            if compare:
                return i
        return None

    def if_ou_get_index(x, y):
        for i in range(len(fresh)):
            compare = (x <= fresh[i][0] and y >= fresh[i][0]) and (
                x <= fresh[i][1] and y >= fresh[i][1]
            )
            if compare:
                return i
        return None

    for ran in range(len(pre_fresh_list)):
        a, b = pre_fresh_list[ran]

        x, y = if_in_get_index(a), if_in_get_index(b)

        if x is not None and y is not None:
            if x > y:
                first = fresh.pop(x)
                second = fresh.pop(y)
            elif x < y:
                second = fresh.pop(y)
                first = fresh.pop(x)
            else:
                first = fresh.pop(x)
                second = first

            a = first[0]
            b = second[1]
        elif x is not None:
            first = fresh.pop(x)
            a = first[0]
        elif y is not None:
            second = fresh.pop(y)
            b = second[1]
        else:
            z = if_ou_get_index(a, b)

            if z is not None:
                cache = fresh.pop(z)

        fresh.append([a, b])

        range_start.append(a)
        range_end.append(b)

    yes_fresh = 0

    for ran in fresh:
        cache = (ran[1] + 1) - ran[0]
        yes_fresh += cache

        if False:  # debug
            print(
                f"\tAdding: {f'{cache:,}'.rjust(19)} | {f'{ran[0]:,}'.rjust(19)} | {f'{ran[1]:,}'.rjust(19)}"
            )

    print(f"Result: {yes_fresh:,}")


if __name__ == "__main__":
    print("-------------")
    start_part1 = time.time()
    part01()
    print(f" -> Needed: {round((time.time() - start_part1) * 1_000_000):,}ns")
    print("-------------")
    start_part2 = time.time()
    part02()
    print(f" -> Needed: {round((time.time() - start_part2) * 1_000_000):,}ns")
