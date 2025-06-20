from common.base_solution import BaseSolution
from utils.bfs_path import BFSPath
import regex as re
import itertools

NUMPAD = [
    ('7', (0, 0)), ('8', (1, 0)), ('9', (2, 0)),
    ('4', (0, 1)), ('5', (1, 1)), ('6', (2, 1)),
    ('1', (0, 2)), ('2', (1, 2)), ('3', (2, 2)),
                   ('0', (1, 3)), ('A', (2, 3)),
]

DIRECTIONAL = [
                   ('^', (1, 0)), ('A', (2, 0)),
    ('<', (0, 1)), ('v', (1, 1)), ('>', (2, 1)),
]

def getAllPaths(
    stuff: list[tuple[str, tuple[int, int]]],
    size: tuple[int, int],
    walls: set[tuple[int, int]],
):
    isLeft  = lambda cur, next: cur[0] - next[0] == 1
    isRight = lambda cur, next: next[0] - cur[0] == 1
    isUp    = lambda cur, next: cur[1] - next[1] == 1
    isDown  = lambda cur, next: next[1] - cur[1] == 1

    paths: dict[tuple[str, str], str] = dict()
    for start, startCoords in stuff:
        for end, endCoords in stuff:
            path = BFSPath(size, walls, startCoords, endCoords)
            command = ""

            for i in range(len(path) - 1):
                cur, next = path[i], path[i + 1]

                if   isLeft(cur, next):  command += '<'
                elif isRight(cur, next): command += '>'
                elif isUp(cur, next):    command += '^'
                elif isDown(cur, next):  command += 'v'

            paths[(start, end)] = command

    return paths

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        numPaths = getAllPaths(NUMPAD,      (3, 4), {(0, 3)})
        dirPaths = getAllPaths(DIRECTIONAL, (3, 2), {(0, 0)})

        r2 = 'A'
        r1 = 'A'
        me = 'A'

        t = 0

        # TODO: Test every combination of commands (ex. >>^ and >^> and ^>>)

        for startCommand in ("029A", "980A", "179A", "456A", "379A"):
            r2Command = "".join(numPaths[(r2, r2 := c)] + 'A' for c in startCommand)
            r1Command = "".join(dirPaths[(r1, r1 := c)] + 'A' for c in r2Command)
            meCommand = "".join(dirPaths[(me, me := c)] + 'A' for c in r1Command)

            print(meCommand)

            t += len(meCommand) * int(re.findall(r"(?<!\d)0*(\d+)", startCommand)[0])

        return NotImplemented

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
