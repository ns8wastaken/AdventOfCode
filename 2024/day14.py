from common.base_solution import BaseSolution
from utils.ivector2 import IVec2
import re

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data = [[IVec2(*map(int, pair.split(","))) for pair in re.findall(r"-?\d+,-?\d+", line)] for line in self.dataRaw.split("\n")]

        width  = 101
        height = 103

        for _ in range(100):
            for robot in data:
                robot[0] += robot[1]
                robot[0].x %= width
                robot[0].y %= height

        # q1 | q2
        # ---+---
        # q3 | q4

        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0

        middleWidth  = width // 2
        middleHeight = height // 2

        for robot in data:
            if robot[0].x == middleWidth or robot[0].y == middleHeight:
                continue

            if robot[0].x < middleWidth and robot[0].y < middleHeight:
                q1 += 1

            elif robot[0].x > middleWidth and robot[0].y < middleHeight:
                q2 += 1

            elif robot[0].x < middleWidth and robot[0].y > middleHeight:
                q3 += 1

            elif robot[0].x > middleWidth and robot[0].y > middleHeight:
                q4 += 1

        return q1 * q2 * q3 * q4

    def Part2(self) -> BaseSolution.ResultType:
        data = [[IVec2(*map(int, pair.split(","))) for pair in re.findall(r"-?\d+,-?\d+", line)] for line in self.dataRaw.split("\n")]

        width  = 101
        height = 103

        for _ in range(1000):
            for robot in data:
                robot[0] += robot[1]
                robot[0].x %= width
                robot[0].y %= height

        # This is big poopoo
        return NotImplemented
