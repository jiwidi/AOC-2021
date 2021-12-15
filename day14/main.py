from collections import Counter


def read_input(path):
    inp = open(path).read()
    template, rules_string = inp.split("\n\n")
    template = [x for x in template]
    rules = {}
    for line in rules_string.split("\n"):
        if line:
            k, v = line.split(" -> ")
            rules[k] = v
    return template, rules


def part_one(parsed_data):
    old_poly, rules = parsed_data
    for step in range(10):
        new_poly = []
        for e_i in range(len(old_poly) - 1):
            new_poly.append(old_poly[e_i])
            new_poly.append(rules[old_poly[e_i] + old_poly[e_i + 1]])
        new_poly.append(old_poly[-1])
        old_poly = new_poly
    cntr = Counter(new_poly)
    counts = cntr.most_common()
    return counts[0][1] - counts[-1][1]


def part_two(parsed_data):
    old_poly, rules = parsed_data
    poly_dict = Counter(map(str.__add__, old_poly, old_poly[1:]))
    elem_count = Counter(old_poly)
    for step in range(40):
        for (elem_1, elem_2), count in poly_dict.copy().items():
            new_elem = rules[elem_1 + elem_2]
            poly_dict[elem_1 + elem_2] -= count
            poly_dict[elem_1 + new_elem] += count
            poly_dict[new_elem + elem_2] += count
            elem_count[new_elem] += count
    return max(elem_count.values()) - min(elem_count.values())


def main():
    inp = read_input("input.txt")
    score1 = part_one(inp)
    score2 = part_two(inp)

    print("Solutions:", score1, score2)


if __name__ == "__main__":
    main()
