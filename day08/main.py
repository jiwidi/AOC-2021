from collections import Counter


def read_input(path):
    lines = open(path).readlines()
    return lines


def solve_first(lines):
    segment = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg",
    }
    # number of segments lit
    seglit = {k: len(v) for k, v in segment.items()}
    s = 0
    t = 0
    for line in lines:
        a, b = line.strip().split("|")
        patterns, values = a.split(), b.split()
        # Part 1
        c = Counter([len(x) for x in values])
        s += sum([c[seglit[1]], c[seglit[4]], c[seglit[7]], c[seglit[8]]])

        # Part 2
        # dict of all 10 numbers as keys and the segments as values
        # e.g.: id[1] = set('c', 'f')
        id = {}
        # 1,4,7,8 can be solely decided on the length of the pattern
        for p in patterns:
            l = len(p)
            p = set(p)
            if l == 2:
                id[1] = p
            elif l == 4:
                id[4] = p
            elif l == 3:
                id[7] = p
            elif l == 7:
                id[8] = p

        # there are two groups left: lengths 5 and 6
        # based on the decoded patterns for 1,4,7 the others can be decoded
        for p in patterns:
            l = len(p)
            p = set(p)
            if l == 6:  # 0,6,9
                if (id[1] | id[4] | id[7]).issubset(p):
                    id[9] = p
                elif (id[1] | id[7]).issubset(p) and not id[4].issubset(p):
                    id[0] = p
                else:
                    id[6] = p
            elif l == 5:  # 2,3,5
                if (id[4] - id[1]).issubset(p):
                    id[5] = p
                elif (id[1] | id[7]).issubset(p):
                    id[3] = p
                else:
                    id[2] = p

        # need to sort the values alphabetically
        # decoder reverses the id dict
        # e.g. decoder["cf"] = 1
        decoder = {"".join(sorted(list(v))): k for k, v in id.items()}
        t += int("".join([str(decoder["".join(sorted(v))]) for v in values]))
    return s, t


def main():
    numbers = read_input("input.txt")
    first_solution, second_solution = solve_first(numbers)

    print("Solutions:", first_solution, second_solution)


if __name__ == "__main__":
    main()
