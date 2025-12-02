def part01():
    print("Advent of Code 2025 Day 2 part 1")

    with open("input", "r") as file_input:
        line = file_input.readlines()[0].replace("\n", "")  # It is all in one line

    ranges = line.split(",")

    sum = 0

    for r in ranges:
        splitted = r.split("-")
        start, end = int(splitted[0]), int(splitted[1])
        for i in range(start, end + 1):
            textnr = str(i)
            if len(textnr) % 2 != 0:
                continue

            half = int(len(textnr) / 2)
            part1 = textnr[:half]
            part2 = textnr[half:]

            if part1 == part2:
                sum += i

    print(" -> Result:", sum)


if __name__ == "__main__":
    part01()
