import numpy as np


def read_input(path):
    inp = np.array(
        [[int(x) for x in line] for line in open(path).read().split("\n") if line]
    )
    return inp


def score(octopus_matrix, steps=0):
    octopi = octopus_matrix.copy()
    total_flashes = 0
    step = 0
    while True:
        octopi += 1
        charged_octopi = np.where(octopi > 9)
        octopi_mask = np.zeros((10, 10))
        while charged_octopi[0].size > 0:
            for row, col in zip(*charged_octopi):
                if octopi_mask[row, col] == 1:
                    continue
                octopi_mask[row, col] = 1
                min_row = row - 1 if row > 0 else row
                max_row = row + 2 if row < 9 else row + 1
                min_col = col - 1 if col > 0 else col
                max_col = col + 2 if col < 9 else col + 1
                octopi[min_row:max_row, min_col:max_col] += 1
            charged_octopi = np.where(np.logical_and(octopi > 9, octopi_mask == 0))
        for row, col in zip(*np.where(octopi_mask == 1)):
            octopi[row, col] = 0
        total_flashes += np.sum(octopi_mask)
        if np.sum(octopi_mask) == 100 or step + 1 == steps:
            return total_flashes, step + 1
        step += 1


def main():
    inp = read_input("input.txt")
    score1 = score(inp, 100)[0]
    score2 = score(inp)[1]

    print("Solutions:", score1, score2)


if __name__ == "__main__":
    main()
