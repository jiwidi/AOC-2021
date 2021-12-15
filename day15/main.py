import heapq
import numpy as np


def read_input(path):
    inp = np.array(
        [[int(x) for x in line] for line in open(path).read().split("\n") if line]
    )
    return inp


class PriorityQueue:
    def __init__(self) -> None:
        self.elements = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def inBounds(pos, width, height):
    x, y = pos
    return 0 <= x < width and 0 <= y < height


def neighbors(pos, width, height):
    x, y = pos
    nb = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
    results = []
    for n in nb:
        if inBounds(n, width, height):
            results.append(n)
    return results


def heuristic(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def solveCave(cave, part2=False):
    def cost(pos):
        x, y = pos
        if not part2:
            return cave[y][x]
        else:
            result = (
                cave[y % tileHeight][x % tileWidth] + x // tileWidth + y // tileHeight
            )
            return result % 9 if result > 9 else result

    width, height = len(cave[0]), len(cave)
    tileWidth, tileHeight = width, height
    if part2:
        width *= 5
        height *= 5

    q = PriorityQueue()
    q.put((0, 0), 0)
    pathRisk = dict()
    pathRisk[(0, 0)] = 0
    goal = (width - 1, height - 1)

    while not q.empty():
        current = q.get()
        if current == goal:
            break
        for nn in neighbors(current, width, height):
            new_cost = pathRisk[current] + cost(nn)
            if nn not in pathRisk or new_cost < pathRisk[nn]:
                pathRisk[nn] = new_cost
                prio = new_cost + heuristic(goal, nn)
                q.put(nn, prio)
    return pathRisk[goal]


def main():
    cave = read_input("input.txt")
    part1 = solveCave(cave)
    part2 = solveCave(cave, True)
    header = "#" * 20
    print(part1, part2)


if __name__ == "__main__":
    main()
