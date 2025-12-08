import math


class Vector:
    x: int = 0
    y: int = 0
    z: int = 0

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def from_string(s: str):
        x = [int(i) for i in s.split(",")]
        v = Vector(x[0], x[1], x[2])
        return v

    def vector_distance(self, a: "Vector") -> float:
        return abs(
            math.sqrt((self.x - a.x) ** 2 + (self.y - a.y) ** 2 + (self.z - a.z) ** 2)
        )

    def __str__(self) -> str:
        return f"Vector: [{self.x},{self.y},{self.z}]"


def part01():
    print("Advent of Code 2025 - Day 08 Part 01")

    with open("input", "r") as file_input:
        vectors: list[Vector] = [Vector.from_string(x) for x in file_input.readlines()]

    pairs: list[list[Vector]] = []

    for vec in range(len(vectors)):
        # index, distance
        nearest: tuple[int, float] = (-1, -1)
        for vec_compare in range(len(vectors)):
            if vec == vec_compare:
                continue

            cache = vectors[vec].vector_distance(vectors[vec_compare])

            if nearest == (-1, -1) or cache < nearest[1]:
                nearest = (vec_compare, cache)

            group = -1
            for i in range(len(pairs)):
                if vectors[vec_compare] in pairs[i]:
                    group = i

            if group == -1:
                pairs.append([vectors[vec_compare]])
                break
            else:
                pairs[group].append(vectors[vec_compare])

        for pair in sorted(pairs, key=lambda x: len(x), reverse=True):
            print(len(pair), [str(x) for x in pair])

        print("#########################")
        print(pairs)
        input()


if __name__ == "__main__":
    print("----------")
    part01()
