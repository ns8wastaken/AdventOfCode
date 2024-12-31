from common.base_solution import BaseSolution
from utils.ivector2 import IVec2
from collections import deque

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        def DFS(graph: list[list[int]], start: IVec2) -> int:
            stack: deque[IVec2] = deque()
            stack.append(start)

            visited = set()
            visited.add(start)

            neighbors = (IVec2(0, 1), IVec2(0, -1), IVec2(1, 0), IVec2(-1, 0))

            score = 0

            while stack:
                current = stack.popleft()

                for n in neighbors:
                    newPos = current + n

                    if (
                        0 <= newPos.x < len(graph[0]) and
                        0 <= newPos.y < len(graph) and
                        (newPos not in visited) and
                        graph[newPos.y][newPos.x] == graph[current.y][current.x] + 1
                    ):
                        visited.add(newPos)
                        stack.append(newPos)

                        if graph[newPos.y][newPos.x] == 9:
                            score += 1

            return score

        d = [list(map(int, i)) for i in self.dataRaw.split("\n")]

        total = 0

        for y in range(len(d)):
            for x in range(len(d[y])):
                if d[y][x] == 0:
                    total += DFS(d, IVec2(x, y))

        return total

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
