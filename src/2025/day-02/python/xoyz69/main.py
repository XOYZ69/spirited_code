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


def part02():
    print("Advent of Code 2025 Day 2 part 2")

    with open("input", "r") as file_input:
        line = file_input.readlines()[0].replace("\n", "")  # It is all in one line

    ranges = line.split(",")

    sum = 0

    for r in ranges:
        splitted = r.split("-")
        start, end = int(splitted[0]), int(splitted[1])
        print("----------------")
        print(start, end)
        for i in range(start, end + 1):
            textnr = str(i)

            section_size = round(len(textnr) / 2)
            invalid = False

            while section_size > 0 and not invalid:
                # print(start, end, i, section_size)
                if len(textnr) % section_size == 0:
                    parts = []
                    works = True
                    for p in range(0, len(textnr), section_size):
                        parts.append(textnr[p : p + section_size])

                        for a in parts:
                            if a != parts[-1]:
                                works = False

                    if works:
                        invalid = True

                section_size -= 1

            # print("\t", invalid)

            if invalid:
                print(f"\tFound invalid id: {i:,}")
                sum += i

    print(f" -> Result: {sum:,}")


if __name__ == "__main__":
    part01()
    part02()
