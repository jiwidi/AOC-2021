# --- Day 5: Hydrothermal Venture ---


def read_input(path):
    lines = open(path).read().splitlines()
    return lines


def solve_first(lines):
    grid = []
    for i in range(len(lines)):
        grid.append(list([0] * len(lines[0])))

    points = {}
    for line in lines:
        l, r = line.split(" -> ")
        x1, y1 = map(int, l.split(","))
        x2, y2 = map(int, r.split(","))

        if y1 == y2:  # Horizontal line
            for i in range(min(x1, x2), max(x1, x2) + 1):
                points[(y1, i)] = points.get((y1, i), 0) + 1

        if x1 == x2:  # Vertical line
            for i in range(min(y1, y2), max(y1, y2) + 1):
                points[(i, x1)] = points.get((i, x1), 0) + 1

    overlap_count = 0
    for i in points.items():
        if i[1] >= 2:
            overlap_count += 1
    return overlap_count


def solve_second(lines):
    grid = []
    for i in range(len(lines)):
        grid.append(list([0] * len(lines[0])))

    points = {}
    for line in lines:
        l, r = line.split(" -> ")
        x1, y1 = map(int, l.split(","))
        x2, y2 = map(int, r.split(","))

        if y1 == y2:  # Horizontal line
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[(y1, x)] = points.get((y1, x), 0) + 1

        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[(y, x1)] = points.get((y, x1), 0) + 1
                # grid[y][x1] += 1

        if not (x1 == x2 or y1 == y2):  # Diagonal line
            dx = x2 - x1
            dy = y2 - y1
            points[(y1, x1)] = points.get((y1, x1), 0) + 1
            while not x1 == x2:
                x1 = x1 + (dx // abs(dx))
                y1 = y1 + (dy // abs(dy))
                points[(y1, x1)] = points.get((y1, x1), 0) + 1

    overlap_count = 0
    for i in points.items():
        if i[1] >= 2:
            overlap_count += 1
    return overlap_count


def main():
    lines = read_input("input.txt")
    first_solution = solve_first(lines)

    second_solution = solve_second(lines)
    print("Solutions:", first_solution, second_solution)


if __name__ == "__main__":
    main()
