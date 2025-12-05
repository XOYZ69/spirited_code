import time


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


if __name__ == "__main__":
    print("-------------")
    start_part1 = time.time()
    part01()
    print(f" -> Needed: {time.time() - start_part1}s")
