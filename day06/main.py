from collections import defaultdict


def read_input(path):
    numbers = open(path).read().replace("\n", "").split(",")
    return [int(x) for x in numbers]


def gift_of_life(numbers, days=80):
    population = defaultdict(int)
    for u in numbers:
        population[u] += 1

    # Iterate each day
    for i in range(days):
        new_population = defaultdict(int)
        # Iterate each number
        for u in population.keys():
            newlife = u - 1
            if newlife >= 0:
                new_population[newlife] += population[u]
            else:  # give birth
                new_population[6] += population[u]
                new_population[8] += population[u]

        population = new_population

    # Count how many we have
    aux = 0
    for u in population.keys():
        aux += population[u]
    return aux


def main():
    numbers = read_input("input.txt")
    first_solution = gift_of_life(numbers, days=80)
    second_solution = gift_of_life(numbers, days=256)

    print("Solutions:", first_solution, second_solution)


if __name__ == "__main__":
    main()
