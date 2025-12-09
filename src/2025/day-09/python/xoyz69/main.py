import time


def part01():
    print("Advent of Code 2025 - Day 09 Part 01")

    with open("input", "r") as file_input:
        rects = [
            [int(char) for char in x.strip().split(",")] for x in file_input.readlines()
        ]

    biggest = (0, 0, 0)  # Index A, Index B, Size

    for a in range(len(rects)):
        for b in range(len(rects)):
            sq = (abs(rects[a][0] - rects[b][0]) + 1) * (
                abs(rects[a][1] - rects[b][1]) + 1
            )

            if rects[a] == [11, 1]:
                print(rects[a], rects[b], sq)

            if sq > biggest[2]:
                biggest = (a, b, sq)

    print(f"Result: {biggest}")


if __name__ == "__main__":
    print("-------------")
    start_part1 = time.time()
    part01()
    print(f" -> Needed: {round((time.time() - start_part1) * 1_000_000):,}ns")
