import numpy as np
from itertools import product


def read_input(path):
    inp = open(path).read()
    algo, image = inp.split("\n\n")
    algo = list(map(int, algo.replace("#", "1").replace(".", "0")))
    image = image.split("\n")
    image = np.array(
        [list(map(int, x.replace("#", "1").replace(".", "0"))) for x in image]
    )

    # Pad
    print(image.shape)
    image = np.pad(image, pad_width=50 * 2, mode="constant", constant_values=0)
    print(image.shape)
    return algo, image


def calculate_algo(submatrix, algo):
    flat = submatrix.flatten()
    decimal_value = int(flat.dot(2 ** np.arange(flat.size)[::-1]))
    return algo[decimal_value]


def enhance_image(image, algo):
    aux_image = np.zeros(image.shape)

    y_range = range(1, aux_image.shape[1] - 1)
    x_range = range(1, aux_image.shape[0] - 1)
    for i, j in product(x_range, y_range):
        submatrix = image[i - 1 : i + 2, j - 1 : j + 2]
        aux_image[i, j] = calculate_algo(submatrix, algo)
    return aux_image


def enhance_image_n(image, algo, n):
    aux_image = image[:]
    for _ in range(n):
        aux_image = enhance_image(aux_image, algo)

    aux_image = aux_image[: -n * 2, : -n * 2]
    return aux_image


def print_image(image):
    print(np.array2string(image, separator="").replace("0.", ".").replace("1.", "#"))


def main():
    algo, image = read_input("input.txt")
    part1 = np.sum(enhance_image_n(image, algo, 2))
    part2 = np.sum(enhance_image_n(image, algo, 50))
    print("Solutions:", part1, part2)


if __name__ == "__main__":
    main()
