data = []

width = 0
height = 0

y = 0
x = 0

with open("data6.txt", "r") as f:
    data = [list(i.strip()) for i in f.readlines()]

    f.seek(0)
    s = f.read()

    width = s.index("\n")
    height = s.count("\n") + 1

    s = s.replace("\n", "")

    x = s.index("^") % width
    y = s.index("^") // width


def Part1(data: list[list[str]]) -> str:
    global width, height, y, x

    soldier = "^"

    while True:
        data[y][x] = "X"

        match soldier:
            case "^":
                if data[y - 1][x] != "#":
                    y -= 1

                else:
                    soldier = ">"

            case "v":
                if data[y + 1][x] != "#":
                    y += 1

                else:
                    soldier = "<"

            case ">":
                if data[y][x + 1] != "#":
                    x += 1

                else:
                    soldier = "v"

            case "<":
                if data[y][x - 1] != "#":
                    x -= 1

                else:
                    soldier = "^"

        if (y == 0) or (y == height - 1) or (x == 0) or (x == height - 1):
            data[y][x] = "X"
            break

    return "".join("".join(i) for i in data)


def Part2():
    global data, width, height, y, x

    visitedSpots = "\n".join("".join(i) for i in Part1(data))

    prevIndex = 0
    for i in range(visitedSpots.count("X")):
        idx = visitedSpots.index("X", prevIndex)

        Part1(data)

        prevIndex = idx + 1

        with open("data6.txt", "r") as f:
            data = [list(i.strip()) for i in f.readlines()]


if __name__ == "__main__":
    # print(Part1(data).count("X"))
    Part2()
