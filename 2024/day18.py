from common.base_solution import BaseSolution
from collections import deque

def BFSPath(
    walls: set[tuple[int, int]],
    start: tuple[int, int],
    end:   tuple[int, int],
) -> int:
    visited: dict[tuple[int, int], tuple[int, int] | None] = { start: None }
    queue = deque([start])

    isInMaze = lambda pos: (0 <= pos[0] <= 70) and (0 <= pos[1] <= 70)

    # BFS
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while queue:
        current = queue.pop()

        if current == end:
            break

        for dx, dy in dirs:
            newPos = (current[0] + dx, current[1] + dy)

            if (newPos in visited) or (newPos in walls) or not isInMaze(newPos):
                continue

            visited[newPos] = current
            queue.appendleft(newPos)

    if end not in visited:
        return 0

    # Reconstruct path
    path = [end]
    while (current := visited[path[-1]]) != None:
        path.append(current)

    return len(path)

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        walls = set()

        lines = self.dataRaw.split('\n')
        for i in range(1024):
            x, y = lines[i].split(',')
            walls.add((int(x), int(y)))

        pathLen = BFSPath(walls, (0, 0), (70, 70))
        return pathLen - 1

    def Part2(self) -> BaseSolution.ResultType:
        walls = set()

        # The first 1024 already work
        lines = self.dataRaw.split('\n')
        for i in range(1024):
            x, y = lines[i].split(',')
            walls.add((int(x), int(y)))

        n = 0
        while BFSPath(walls, (0, 0), (70, 70)) != 0:
            x, y = lines[n].split(',')
            walls.add((int(x), int(y)))
            n += 1

        return lines[n - 1]
