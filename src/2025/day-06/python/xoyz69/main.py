import time
from linecache import cache


def part01():
    print("Advent of Code 2025 - Day 6 Part 1")

    with open("input", "r") as file_input:
        lines = file_input.readlines()
        operations = lines.pop(-1).split()
        numbers = [[int(x) for x in line.split()] for line in lines]

    res = 0
    for i in range(len(operations)):
        op = operations[i]
        cache = 0
        for n in numbers:
            if op == "+":
                cache += n[i]
            else:
                if cache == 0:
                    cache = n[i]
                else:
                    cache *= n[i]
        res += cache

    print(f"Result: {res}")


def part02():
    print("Advent of Code 2025 - Day 6 Part 1")

    with open("input", "r") as file_input:
        lines = file_input.readlines()
        operations = lines.pop(-1).split()
        numbers = [line.replace("\n", "") for line in lines]

    res = 0

    max_length = 0
    for i in numbers:
        if len(i) > max_length:
            max_length = len(i)

    op_index = 0
    cache_num = 0
    for i in range(max_length):
        n = ""
        for j in range(len(numbers)):
            n += numbers[j][i] if i < len(numbers[j]) else ""
        if n.strip() == "":
            op_index += 1
            res += cache_num
            cache_num = 0
            continue
        if operations[op_index] == "+":
            cache_num += int(n.strip())
        else:
            if cache_num == 0:
                cache_num = int(n.strip())
            else:
                cache_num *= int(n.strip())

    res += cache_num

    print(f"Result: {res}")


if __name__ == "__main__":
    print("-------------")
    start_part1 = time.time()
    part01()
    print(f" -> Needed: {round((time.time() - start_part1) * 1_000_000):,}ns")
    print("-------------")
    start_part2 = time.time()
    part02()
    print(f" -> Needed: {round((time.time() - start_part2) * 1_000_000):,}ns")
