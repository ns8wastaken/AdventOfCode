from common.base_solution import BaseSolution
from utils.bfs_maze import BFSMaze


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
        height = len(lines)
        width = len(lines[0])
        for y in range(height):
            for x in range(width):
                c = lines[y][x]
                pos = (x, y)
                if   c == '#': walls.add(pos)
                elif c == 'S': start = pos
                elif c == 'E': end = pos

        t = 0

        base = len(BFSMaze((width, height), walls, start, end)[1:])
        for w in walls:
            walls2 = walls.copy()
            walls2.remove(w)
            path = BFSMaze((width, height), walls2, start, end)[1:]

            if base - len(path) >= 100:
                t += 1

        return NotImplemented

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
