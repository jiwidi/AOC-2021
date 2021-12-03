import numpy as np


def read_input(path):
    return [[int(i) for i in x.replace("\n", "")] for x in open(path)]


def solve_first(input):
    aux = np.array(input)
    aux = np.average(aux, axis=0)
    gamma = np.rint(aux).astype(int)
    epsilon = np.logical_not(gamma).astype(int)

    gamma = gamma.dot(2 ** np.arange(gamma.size)[::-1])
    epsilon = epsilon.dot(2 ** np.arange(epsilon.size)[::-1])

    return gamma, epsilon


def solve_second(input):
    oxygen = np.copy(input)
    co = np.copy(input)
    for i in range(len(input[0])):
        # Oxygen
        if len(oxygen) > 1:
            aux = np.average(oxygen, axis=0)
            if aux[i] == 0.5:
                aux[i] = 1

            firstbit = np.rint(aux).astype(int)[i]

            oxygen = oxygen[np.where(oxygen[:, i] == firstbit)]

        # CO
        if len(co) > 1:
            aux = np.average(co, axis=0)
            if aux[i] == 0.5:
                aux[i] = 1
            firstbit = np.rint(aux).astype(int)[i]
            firstbit = int(not firstbit)
            co = co[np.where(co[:, i] == firstbit)]

    oxygen = oxygen[0]
    co = co[0]
    print("oxygen:", oxygen)
    print("co:", co)

    oxygen = oxygen.dot(2 ** np.arange(oxygen.size)[::-1])
    co = co.dot(2 ** np.arange(co.size)[::-1])

    return oxygen, co


def main():
    problem_input = read_input("input.txt")
    gamma, epislon = solve_first(problem_input)
    print(
        f"Solution first problem: gamma:{gamma} - epsilon:{epislon} - multiply:{gamma * epislon}"
    )
    oxygen, co = solve_second(problem_input)
    print(
        f"Solution second problem: oxygen:{oxygen} - co:{co} - multiply:{oxygen * co}"
    )


if __name__ == "__main__":
    main()
