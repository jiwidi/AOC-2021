def read_input(path):
    return [int(x) for x in open(path)]


def find_increases(sonar_output):
    increases = 0
    for u in range(1, len(sonar_output)):
        if sonar_output[u - 1] < sonar_output[u]:
            increases += 1
    return increases


def find_increases_windowed(sonar_output):
    # We create the windows
    windows = []
    for u in range(len(sonar_output) - 2):
        window = sonar_output[u] + sonar_output[u + 1] + sonar_output[u + 2]
        windows.append(window)
    increases = find_increases(windows)
    return increases


def main():
    sonar_output = read_input("input.txt")
    increases = find_increases(sonar_output)
    print("Number of basic increases", increases)
    increases = find_increases_windowed(sonar_output)
    print("Number of window increases", increases)


if __name__ == "__main__":
    main()
