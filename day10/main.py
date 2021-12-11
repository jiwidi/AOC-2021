from functools import reduce

open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
score1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
score2 = {"(": 1, "[": 2, "{": 3, "<": 4}


def score(l, stack, corrupted=True):
    if not l:
        return (not corrupted) * reduce(lambda x, y: 5 * x + score2[y], stack[::-1], 0)
    elif l[0] in open_to_close:
        return score(l[1:], [*stack, l[0]], corrupted)
    elif open_to_close[stack[-1]] == l[0]:
        return score(l[1:], stack[:-1], corrupted)
    else:
        return corrupted * score1[l[0]]


def read_input(path):
    inp = open(path).read().splitlines()
    return inp


def main():
    inp = read_input("input.txt")
    scores2 = sorted(filter(None, [score(l, [], False) for l in inp]))
    score1 = sum(score(l, []) for l in inp)
    score2 = scores2[len(scores2) // 2]

    print("Solutions:", score1, score2)


if __name__ == "__main__":
    main()
