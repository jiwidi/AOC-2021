def read_input(path):
    return [x for x in open(path)]


def modify_position_dummy(position, instruction):
    ins_type = instruction.split(" ")[0]
    ins_value = int(instruction.split(" ")[1].replace("\n", ""))

    if ins_type == "forward":
        position[0] += ins_value
    elif ins_type == "up":
        position[1] -= ins_value
    elif ins_type == "down":
        position[1] += ins_value
    return position


def modify_position_smart(position, instruction):
    ins_type = instruction.split(" ")[0]
    ins_value = int(instruction.split(" ")[1].replace("\n", ""))

    if ins_type == "forward":
        position[0] += ins_value
        position[1] += ins_value * position[2]
    elif ins_type == "up":
        position[2] -= ins_value
    elif ins_type == "down":
        position[2] += ins_value

    return position


def find_position(input):
    first_position = [0, 0]  # Horizontal, depth, aim
    second_position = [0, 0, 0]  # Horizontal, depth, aim
    for instruction in input:
        first_position = modify_position_dummy(first_position, instruction)
        print(second_position)
        second_position = modify_position_smart(second_position, instruction)

    return first_position, second_position


def main():
    problem_input = read_input("input.txt")
    first_position, second_position = find_position(problem_input)
    print("First position", first_position, first_position[0] * first_position[1])
    print("Second position", second_position, second_position[0] * second_position[1])


if __name__ == "__main__":
    main()
