import numpy as np
import itertools
from scipy.spatial.distance import cdist


def read_input(path):
    r = []
    inp = open(path).read()

    for scanner in inp.split("\n\n"):
        aux = scanner.split("\n")
        scanner = np.array([list(map(int, x.split(","))) for x in aux[1:]])

        r.append(scanner)
    return r


def remap(scanner):
    """
    Remap the scanner to the origin
    """
    return scanner - scanner[0]


def get_rotations(scanner):
    ##Rotate 24 times
    transforms = [
        (1, 1, 1),
        (1, 1, -1),
        (1, -1, 1),
        (1, -1, -1),
        (-1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (-1, -1, -1),
    ]

    remaps = [(0, 1, 2), (1, 2, 0), (2, 1, 0), (2, 0, 1), (1, 0, 2), (0, 2, 1)]
    r = [
        scanner[:][:, remap] * transform
        for transform, remap in itertools.product(transforms, remaps)
    ]
    return r


def row_check(matrixa, matrixb):
    """
    Returns the number of overlapping elements between two matrices
    """
    return sum(np.isin(matrixb, matrixa).all(axis=1))


def row_add(matrixa, matrixb):
    """
    Concats all non duplicate rows from two matrixes
    """
    aux_a = matrixa[:]
    aux_b = matrixb[:].tolist()
    slices = []
    for i in range(len(matrixa)):
        if any((aux_b == matrixa[i]).all(1)):
            slices.append(i)

    aux_a = np.delete(aux_a, slices, 0)
    return np.vstack((aux_a, matrixb[:]))


def check_overlap(scanner_one, scanner_two, n=12):
    aux = scanner_one[:]
    for i in range(len(scanner_one)):
        for j in range(len(scanner_two)):
            # Join in two points, add the distance to rest of the points
            distance = scanner_one[i] - scanner_two[j]
            aux_two = scanner_two[:] + distance
            overlapping = row_check(aux, aux_two)
            if overlapping >= n:
                return (
                    True,
                    scanner_one[i] - scanner_two[j],
                    aux_two,
                )  # Scanner two respect to scanner one
    return False, None, None


def check_all_overlaps(scanner_one, scanner_two, n=12):
    aux_a = scanner_one[:]
    aux_b = scanner_two[:]
    possible_transforms = get_rotations(aux_b)
    for transform in possible_transforms:
        check, scanner_coor, points = check_overlap(aux_a, transform, n=n)
        if check:
            return check, scanner_coor, points
    return False, None, None


def part_one(scanners):
    # Fill the map until no scanner is left unmatched
    map = np.zeros((10000, 10000, 10000))
    # Initialize the map with the first scanner
    for point in scanners[0]:
        map[point[0]][point[1]][point[2]] = 1

    master_scanner = scanners[0]
    candidates = list(range(1, len(scanners)))
    scanner_coords = []
    while len(candidates) > 0:
        print("Left unmatched scanners:", candidates)
        for idx, j in enumerate(candidates):
            print("checking", j)
            check, scanner_coor, points = check_all_overlaps(
                master_scanner, scanners[j]
            )
            if check:
                print("Bingo - Beacons up to now:", scanner_coor)
                for point in points:
                    map[point[0]][point[1]][point[2]] = 1
                master_scanner = row_add(master_scanner, points)
                candidates.pop(idx)
                print(len(master_scanner))
                scanner_coords.append(scanner_coor)

    return len(master_scanner), scanner_coords


def manhattan_distance(a, b):
    return np.abs(a - b).sum()


def part_two(scanner_coords):
    max_distance = 0
    for i in range(len(scanner_coords)):
        for j in range(len(scanner_coords)):
            dist = manhattan_distance(scanner_coords[i], scanner_coords[j])
            if dist > max_distance:
                max_distance = dist
    return max_distance


def main():
    inp = read_input("input.txt")
    probes, scanner_coords = part_one(inp)
    sol2 = part_two(scanner_coords)
    print("Solutions:", probes, sol2)


if __name__ == "__main__":
    main()
