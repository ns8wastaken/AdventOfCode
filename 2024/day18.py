from common.base_solution import BaseSolution
from utils.bfs_maze import BFSMaze

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        walls = set()

        lines = self.dataRaw.split('\n')
        for i in range(1024):
            x, y = lines[i].split(',')
            walls.add((int(x), int(y)))

        pathLen = len(BFSMaze((71, 71), walls, (0, 0), (70, 70)))
        return pathLen - 1

    def Part2(self) -> BaseSolution.ResultType:
        walls = set()

        # The first 1024 already work
        lines = self.dataRaw.split('\n')
        for i in range(1024):
            x, y = lines[i].split(',')
            walls.add((int(x), int(y)))

        n = 0
        while BFSMaze((71, 71), walls, (0, 0), (70, 70)) != 0:
            x, y = lines[n].split(',')
            walls.add((int(x), int(y)))
            n += 1

        return lines[n - 1]
