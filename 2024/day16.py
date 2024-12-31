from common.base_solution import BaseSolution
from utils.ivector2 import IVec2
import heapq
import time

class Node:
    def __init__(self, cost: int, pos: IVec2, direction: IVec2):
        self.cost = cost
        self.pos = pos
        self.direction = direction

    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash((self.cost, self.pos, self.direction))

class Solution(BaseSolution):
    def DijkstraScore(self, start: IVec2, end: IVec2, walls: set[IVec2]) -> int:
        visited = set()

        queue = [Node(0, start, IVec2(1, 0))]

        directions = (IVec2(0, 1), IVec2(0, -1), IVec2(1, 0), IVec2(-1, 0))

        while len(queue) != 0:
            current = heapq.heappop(queue)
            visited.add(current.pos)

            if current.pos == end:
                return current.cost

            for newDir in directions:
                newPos = current.pos + newDir

                if newPos in walls:   continue
                if newPos in visited: continue

                newCost = current.cost + (1 if current.direction == newDir else 1001)

                heapq.heappush(queue, Node(newCost, newPos, newDir))

        return -1

    def Part1(self) -> BaseSolution.ResultType:
        start = IVec2(0, 0)
        end   = IVec2(0, 0)

        walls: set[IVec2] = set()

        for y, row in enumerate(self.dataRaw.split("\n")):
            for x, c in enumerate(row):
                match c:
                    case "#":
                        walls.add(IVec2(x, y))

                    case "S":
                        start = IVec2(x, y)

                    case "E":
                        end = IVec2(x, y)

        return self.DijkstraScore(start, end, walls)

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
