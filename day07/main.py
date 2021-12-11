import numpy as np


def read_input(path):
    numbers = open(path).read().replace("\n", "").split(",")
    return [int(x) for x in numbers]


def solve_first(numbers):
    r = [[sum([abs(x - z) for z in numbers])] for x in range(0, max(numbers) + 1)]
    return min(r)


def solve_second(numbers):
    r = [
        [sum([abs(x - z) / 2 * (2 + (abs(x - z) - 1)) for z in numbers])]
        for x in range(0, max(numbers) + 1)
    ]
    return min(r)


def main():
    numbers = read_input("input.txt")
    first_solution = solve_first(numbers)
    second_solution = solve_second(numbers)

    print("Solutions:", first_solution, second_solution)


if __name__ == "__main__":
    main()
