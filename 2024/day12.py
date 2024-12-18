from common.base_solution import BaseSolution
from utils.ivector2 import IVec2
from collections import deque

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        def BFSPerimeter(graph: list[list[str]], start: IVec2) -> tuple[int, set[IVec2]]:
            char = graph[start.y][start.x]

            visited: set[IVec2] = set()
            visited.add(start)

            stack: deque[IVec2] = deque()
            stack.append(start)

            neighbors = (IVec2(0, 1), IVec2(0, -1), IVec2(1, 0), IVec2(-1, 0))

            perimeter = 0

            while stack:
                currentPos = stack.popleft()

                for n in neighbors:
                    newPos = currentPos + n

                    if (
                        (not (0 <= newPos.x < len(graph[0])) or not (0 <= newPos.y < len(graph))) or
                        graph[newPos.y][newPos.x] != char
                    ):
                        perimeter += 1

                    elif (newPos not in visited) and (graph[newPos.y][newPos.x] == char):
                        visited.add(newPos)
                        stack.append(newPos)

            return (perimeter, visited)

        d = [list(i) for i in self.dataRaw.split("\n")]

        total = 0

        visited: set[IVec2] = set()
        i = 0
        while i < len(d) * len(d[0]):
            pos = IVec2(i % len(d[0]), i // len(d))

            if pos not in visited:
                perim, v = BFSPerimeter(d, pos)
                total += perim
                visited.union(v)

            i += 1

        return total

    def Part2(self) -> BaseSolution.ResultType:
        pass
