from common.base_solution import BaseSolution
import itertools as it

class Solution(BaseSolution):
    def Part1(self) -> int:
        parsedData = [(int(line[:(i := line.find(":"))]), list(map(int, line[i+2:].strip().split(" ")))) for line in self.dataRaw.split("\n")]

        operators = ["+",  "*"]

        total = 0

        for result, nums in parsedData:
            for test in list(it.product(operators, repeat=len(nums) - 1)):
                t = nums[0]

                for i in range(len(nums) - 1):
                    match test[i]:
                        case "+": t += nums[i + 1]
                        case "*": t *= nums[i + 1]

                if t == result:
                    total += t
                    break

        return total

    def Part2(self) -> int:
        parsedData = [(int(line[:(i := line.find(":"))]), list(map(int, line[i+2:].strip().split(" ")))) for line in self.dataRaw.split("\n")]

        operators = ["+",  "*", "|"]

        total = 0

        for result, nums in parsedData:
            for test in list(it.product(operators, repeat=len(nums) - 1)):
                temp = 0
                t = nums[0]

                for i in range(len(nums) - 1):
                    if temp != 0:
                        t = temp
                        temp = 0

                    match test[i]:
                        case "+": t += nums[i + 1]
                        case "*": t *= nums[i + 1]
                        case "|": temp = int(str(t) + str(nums[i + 1]))

                if temp != 0:
                    t = temp

                if t == result:
                    total += t
                    break

        return total
