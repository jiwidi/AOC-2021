from collections import defaultdict
import numpy as np


def read_input(path):
    input_data = open(path).read()
    coord_string, fold_string = input_data.split("\n\n")
    coords = np.array(
        [
            [int(coord.split(",")[1]), int(coord.split(",")[0])]
            for coord in coord_string.split("\n")
        ]
    )
    paper = np.zeros(
        (np.max(coords[:, 0]) + 1, np.max(coords[:, 1]) + 1), dtype="ubyte"
    )
    paper[coords[:, 0], coords[:, 1]] = 1
    folds = [
        (a_p.split("=")[0].split("fold along ")[1], int(a_p.split("=")[1]))
        for a_p in fold_string.split("\n")
        if a_p
    ]
    return paper, folds


def part_one(parsed_data):
    paper, folds = parsed_data
    axis, pos = folds[0]
    if axis == "x":
        paper = paper[:, :pos] + np.flip(paper[:, pos + 1 :], axis=1)
    else:
        flipped = np.flip(paper[pos + 1 :], axis=0)
        paper = paper[:pos] + flipped
    paper = (paper > 0).astype("ubyte")
    return np.sum(paper)


def part_two(parsed_data):
    paper, folds = parsed_data
    for axis, pos in folds:
        if axis == "x":
            paper = paper[:, :pos] + np.flip(paper[:, pos + 1 :], axis=1)
        else:
            flipped = np.flip(paper[pos + 1 :], axis=0)
            paper = paper[:pos] + flipped
        paper = (paper > 0).astype("ubyte")
    print(
        "\n"
        + np.array2string(
            paper, separator="", formatter={"int": {0: " ", 1: "\u2588"}.get}
        )
    )
    return np.sum(paper)


def main():
    inp = read_input("input.txt")
    score1 = part_one(inp)
    score2 = part_two(inp)

    print("Solutions:", score1, score2)


if __name__ == "__main__":
    main()
