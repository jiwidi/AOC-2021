import numpy as np


def read_input(path):
    numbers = open(path).read().splitlines()
    return numbers


def solve_first(numbers):
    rows, cols = len(numbers), len(numbers[0])
    sum_lowest = 0
    for r in range(rows):
        for c in range(cols):
            min_neighbour = min(
                numbers[r + dr][c + dc]
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= r + dr < rows and 0 <= c + dc < cols
            )
            if numbers[r][c] < min_neighbour:
                sum_lowest += int(numbers[r][c]) + 1
    return sum_lowest


def solve_second(numbers):
    rows, cols = len(numbers), len(numbers[0])
    visited = [[False] * cols for _ in range(rows)]

    def _visit_dfs(r, c):
        size, visited[r][c] = 1, True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and numbers[nr][nc] != "9"
                and not visited[nr][nc]
            ):
                size += _visit_dfs(nr, nc)
        return size

    basins = []
    for r in range(rows):
        for c in range(cols):
            if numbers[r][c] != "9" and not visited[r][c]:
                basins.append(_visit_dfs(r, c))
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


def main():
    numbers = read_input("input.txt")
    first_solution = solve_first(numbers)
    second_solution = solve_second(numbers)

    print("Solutions:", first_solution, second_solution)


if __name__ == "__main__":
    main()
