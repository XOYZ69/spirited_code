def part01():
    print("Advent of Code 2025 - Day 04 Part 01")

    with open("input", "r") as file_input:
        matrix = file_input.readlines()

        for line in matrix:
            line = line.replace("\n", "")

    working_count = 0

    def getIndex(x, y):
        nonlocal matrix

        if x < 0 or x >= len(matrix):
            return 0

        if y < 0 or y >= len(matrix[x]):
            return 0

        return matrix[x][y]

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            cache = [
                [getIndex(x - 1, y - 1), getIndex(x, y - 1), getIndex(x + 1, y - 1)],
                [getIndex(x - 1, y), 0, getIndex(x + 1, y)],
                [getIndex(x - 1, y + 1), getIndex(x, y + 1), getIndex(x + 1, y + 1)],
            ]

            adjacent = sum([x.count("@") for x in cache])

            if adjacent < 4 and matrix[x][y] == "@":
                working_count += 1

    print(f"Result: {working_count}")


def part02():
    print("Advent of Code 2025 - Day 04 Part 01")

    with open("input", "r") as file_input:
        matrix: list[list] = [list(x.replace("\n", "")) for x in file_input.readlines()]

    working_count = 0

    def getIndex(x, y):
        nonlocal matrix

        if x < 0 or x >= len(matrix):
            return 0

        if y < 0 or y >= len(matrix[x]):
            return 0

        return matrix[x][y]

    able_to_remove = True

    while able_to_remove:
        able_to_remove = False
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                cache = [
                    [
                        getIndex(x - 1, y - 1),
                        getIndex(x, y - 1),
                        getIndex(x + 1, y - 1),
                    ],
                    [getIndex(x - 1, y), 0, getIndex(x + 1, y)],
                    [
                        getIndex(x - 1, y + 1),
                        getIndex(x, y + 1),
                        getIndex(x + 1, y + 1),
                    ],
                ]

                adjacent = sum([x.count("@") for x in cache])

                if adjacent < 4 and matrix[x][y] == "@":
                    working_count += 1
                    matrix[x][y] = "."
                    able_to_remove = True

    print(f"Result: {working_count}")


if __name__ == "__main__":
    print("-------")
    part01()
    print("-------")
    part02()
