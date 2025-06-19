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

class Maze:
    def __init__(self, input_: str):
        self.start = IVec2(0, 0)
        self.end   = IVec2(0, 0)

        self.walls: set[IVec2] = set()

        for y, row in enumerate(input_.split("\n")):
            for x, c in enumerate(row):
                match c:
                    case "#":
                        self.walls.add(IVec2(x, y))

                    case "S":
                        self.start = IVec2(x, y)

                    case "E":
                        self.end = IVec2(x, y)

def DijkstraScore(maze: Maze) -> int:
    visited = set()
    queue = [Node(0, maze.start, IVec2(1, 0))]

    directions = (IVec2(0, 1), IVec2(0, -1), IVec2(1, 0), IVec2(-1, 0))

    while len(queue) != 0:
        current = heapq.heappop(queue)
        visited.add(current.pos)

        if current.pos == maze.end:
            return current.cost

        for newDir in directions:
            newPos = current.pos + newDir

            if newPos in maze.walls: continue
            if newPos in visited:    continue

            newCost = current.cost + (1 if current.direction == newDir else 1001)

            heapq.heappush(queue, Node(newCost, newPos, newDir))

    return -1

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        return DijkstraScore(Maze(self.dataRaw))

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
