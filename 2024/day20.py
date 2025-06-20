from common.base_solution import BaseSolution
from utils.bfs_path import BFSPath


class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
#         self.dataRaw = """\
# ###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""
        walls = set()
        start = (0, 0)
        end = (0, 0)

        lines = self.dataRaw.split('\n')
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                c = lines[y][x]
                pos = (x, y)
                if   c == '#': walls.add(pos)
                elif c == 'S': start = pos
                elif c == 'E': end = pos

        t = 0

        base = len(BFSPath(walls, start, end)[1:])
        for w in walls:
            walls2 = walls.copy()
            walls2.remove(w)
            path = BFSPath(walls2, start, end)[1:]

            if base - len(path) >= 100:
                t += 1

        return NotImplemented

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
