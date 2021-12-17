TARGET_X = [85, 145]
TARGET_Y = [-163, -108]


# TARGET_X = [20, 30]
# TARGET_Y = [-10, -5]


def checkPosition(position):
    x, y = position
    if x <= TARGET_X[1] and x >= TARGET_X[0] and y <= TARGET_Y[1] and y >= TARGET_Y[0]:
        return True
    else:
        return False


def solveProbe(initial_position, initial_speed, max_steps=9999):
    position = initial_position[:]
    speed = initial_speed[:]
    i = 0
    highest_y = 0
    while (
        not checkPosition(position)
        and i < max_steps
        and position[1] > TARGET_Y[0]
        and position[0] < TARGET_X[1]
    ):
        position[0] += speed[0]  # x
        position[1] += speed[1]  # y
        # Drag
        speed[0] = speed[0] - 1 if speed[0] > 0 else speed[0] + 1 if speed[0] < 0 else 0
        speed[1] = speed[1] - 1

        if position[1] > highest_y:
            highest_y = position[1]
        i += 1

    if checkPosition(position):
        return True, highest_y

    return False, highest_y


def bruteProbe():
    max_speed = 500
    highest_y = 0
    c = 0
    r = []
    for i in range(TARGET_X[1] + 1):
        for j in range(-max_speed, max_speed):
            speed = [i, j]
            result, highest_y_aux = solveProbe(
                initial_position=[0, 0], initial_speed=speed
            )
            if result:
                c += 1
                if highest_y_aux > highest_y:
                    highest_y = highest_y_aux
    return highest_y, c


def main():
    print(bruteProbe())


if __name__ == "__main__":
    main()
