from common.base_solution import BaseSolution
from utils.ivector2 import IVec2
from collections import deque

class Solution(BaseSolution):
    def getWallsAndVisited(self, dataRaw: str) -> tuple[set[IVec2], set[IVec2]]:
        width = dataRaw.find("\n")
        height = dataRaw.count("\n") + 1

        data = dataRaw.replace("\n", "")
        n = data.find("^")
        robotPos = IVec2(n % width, n // height)
        robotDir = "^"

        walls = set()

        for i, c in enumerate(data):
            if c == "#":
                walls.add(IVec2(i % width, i // height))

        up = IVec2(0, -1)
        down = IVec2(0, 1)
        left = IVec2(-1, 0)
        right = IVec2(1, 0)

        visited = set()
        visited.add(robotPos.copy())

        while (0 <= robotPos.x < width) and (0 <= robotPos.y < height):
            match robotDir:
                case "^":
                    if robotPos + up in walls:
                        robotDir = ">"

                    else:
                        robotPos += up
                        visited.add(robotPos.copy())

                case ">":
                    if robotPos + right in walls:
                        robotDir = "v"

                    else:
                        robotPos += right
                        visited.add(robotPos.copy())

                case "v":
                    if robotPos + down in walls:
                        robotDir = "<"

                    else:
                        robotPos += down
                        visited.add(robotPos.copy())

                case "<":
                    if robotPos + left in walls:
                        robotDir = "^"

                    else:
                        robotPos += left
                        visited.add(robotPos.copy())

        return (walls, visited)

    def Part1(self) -> BaseSolution.ResultType:
        return len(self.getWallsAndVisited(self.dataRaw)[1]) - 1

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
