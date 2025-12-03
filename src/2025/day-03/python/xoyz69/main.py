import math
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

    needed_length = 12

    for linex in tqdm(range(len(lines))):
        line = lines[linex].strip()

        biggest = "0"
        line_length = len(line)

        def backtrack(start_idx, chosen_len, partial_num_str):
            nonlocal biggest

            # If reached needed length, update biggest if bigger
            if chosen_len == needed_length:
                if partial_num_str > biggest:
                    biggest = partial_num_str
                return

            # Prune if partial_num_str is lex smaller than biggest prefix of same length
            # If biggest starts with partial_num_str or partial_num_str > biggest prefix then continue
            length_so_far = len(partial_num_str)
            if (
                biggest[:length_so_far] == partial_num_str
                or partial_num_str > biggest[:length_so_far]
            ):
                # Iterate remaining indices
                remaining_positions = needed_length - chosen_len
                # Optimization: avoid useless looping by checking if enough chars remain
                max_start = line_length - remaining_positions
                for next_idx in range(start_idx, max_start + 1):
                    backtrack(
                        next_idx + 1, chosen_len + 1, partial_num_str + line[next_idx]
                    )
            else:
                # Prune branch early
                return

        backtrack(0, 0, "")

        # print(f"\t Result: {biggest}")
        total_joltage += int(biggest)

    print(f"Result: {total_joltage}")


if __name__ == "__main__":
    print("----------")
    part01()
    print("----------")
    part02()
