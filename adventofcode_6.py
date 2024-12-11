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

soldier = "^"
iscross = False

while True:
    match soldier:
        case "^":
            if data[y - 1][x] != "#":
                if data[y][x] != "+":
                    data[y][x] = "|"
                y -= 1

            else:
                soldier = ">"

        case "v":
            if data[y + 1][x] != "#":
                if data[y][x] != "+":
                    data[y][x] = "|"
                y += 1

            else:
                soldier = "<"

        case ">":
            if data[y][x + 1] != "#":
                if data[y][x] != "+":
                    data[y][x] = "-"
                x += 1

            else:
                soldier = "v"

        case "<":
            if data[y][x - 1] != "#":
                if data[y][x] != "+":
                    data[y][x] = "-"
                x -= 1

            else:
                soldier = "^"

    match soldier:
        case "^":
            if data[y][x] == "-":
                data[y][x] = "+"

        case "v":
            if data[y][x] == "-":
                data[y][x] = "+"

        case ">":
            if data[y][x] == "|":
                data[y][x] = "+"

        case "<":
            if data[y][x] == "|":
                data[y][x] = "+"

    if (y == 0) or (y == height - 1) or (x == 0) or (x == height - 1):
        match soldier:
            case "^":
                data[y][x] = "|"

            case "v":
                data[y][x] = "|"

            case ">":
                data[y][x] = "-"

            case "<":
                data[y][x] = "-"
        break

for i in data:
    print(*i, sep="")

print("".join(["".join(i) for i in data]).count("+"))
