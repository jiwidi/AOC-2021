from collections import defaultdict


def read_input(path):
    inp = open(path).read()
    ave_mapper = defaultdict(list)
    for line in inp.split("\n"):
        if line:
            start_node, end_node = line.split("-")
            ave_mapper[start_node].append(end_node)
            ave_mapper[end_node].append(start_node)
    return ave_mapper


def part_one(parsed_data):
    path_tracker = []
    final_paths = []
    # Add first parts
    for option in parsed_data["start"]:
        current_path = ["start", option]
        path_tracker.append(current_path)
    while path_tracker:
        current_path = path_tracker.pop()
        options = parsed_data[current_path[-1]]
        for option in options:
            if option == "end":
                final_paths.append(current_path + [option])
            elif option.isupper() or option not in current_path:
                path_tracker.append(current_path + [option])
    return len(final_paths)


def part_two(parsed_data):
    path_tracker = []
    final_paths = []
    for option in parsed_data["start"]:
        path_tracker.append({"path": ["start", option], "twice": False})
    while path_tracker:
        current_path = path_tracker.pop()
        options = parsed_data[current_path["path"][-1]]
        for option in options:
            if option == "end":
                final_paths.append(
                    {
                        "path": current_path["path"] + [option],
                        "twice": current_path["twice"],
                    }
                )
            elif option.isupper() or option not in current_path["path"]:
                path_tracker.append(
                    {
                        "path": current_path["path"] + [option],
                        "twice": current_path["twice"],
                    }
                )
            elif not current_path["twice"] and option != "start":
                path_tracker.append(
                    {"path": current_path["path"] + [option], "twice": True}
                )
    return len(final_paths)


def main():
    inp = read_input("input.txt")
    score1 = part_one(inp)
    score2 = part_two(inp)

    print("Solutions:", score1, score2)


if __name__ == "__main__":
    main()
