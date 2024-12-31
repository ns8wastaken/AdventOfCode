from common.base_solution import BaseSolution
from utils.ivector2 import IVec2

class Solution(BaseSolution):
    def move(self, boxes: list[IVec2], walls: list[IVec2], robotPos: IVec2, unitVector: IVec2):
        if robotPos + unitVector in walls:
            return

        boxPositions: list[IVec2] = []

        i = 1
        while (newPos := (robotPos + unitVector * i)) in boxes:
            boxPositions.append(newPos)
            i += 1

        if robotPos + unitVector * i in walls:
            return

        for i in range(len(boxes)):
            if boxes[i] in boxPositions:
                boxes[i] += unitVector

        robotPos += unitVector

        return

    def Part1(self) -> BaseSolution.ResultType:
        mapText, instructions = self.dataRaw.split("\n\n")
        map = list(line for line in mapText.split("\n"))
        width  = len(map[0])
        height = len(map)

        n = mapText.replace("\n", "").find("@")
        robotPos = IVec2(n // width, n % width)

        walls: list[IVec2] = []
        boxes: list[IVec2] = []

        for y in range(height):
            for x in range(width):
                if map[y][x] == "#":
                    walls.append(IVec2(x, y))

                if map[y][x] == "O":
                    boxes.append(IVec2(x, y))


        for c in instructions:
            match c:
                case "<":
                    self.move(boxes, walls, robotPos, IVec2(-1, 0))

                case ">":
                    self.move(boxes, walls, robotPos, IVec2(1, 0))

                case "^":
                    self.move(boxes, walls, robotPos, IVec2(0, -1))

                case "v":
                    self.move(boxes, walls, robotPos, IVec2(0, 1))

        total = 0

        for box in boxes:
            total += 100 * box.y + box.x

        return total

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
