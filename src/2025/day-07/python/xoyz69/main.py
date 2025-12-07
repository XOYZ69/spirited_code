def part01():
    print("Advent of Code 2025 - Day 07 Part 01")

    with open("input", "r") as file_input:
        lines = file_input.readlines()

    s = lines[0].find("S")
    beams = [s]

    score = 0

    for line in lines:
        new_beam = []
        for beam in set(beams):
            if line[beam] == "." or line[beam] == "S":
                new_beam.append(beam)
            elif line[beam] == "^":
                new_beam.append(beam - 1)
                new_beam.append(beam + 1)
                score += 1
            else:
                print(line[beam])
        beams = new_beam

    print(f"Result: {score}")


if __name__ == "__main__":
    print("---------")
    part01()
