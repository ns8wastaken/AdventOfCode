from common.base_solution import BaseSolution
import math

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        instructions, nodes_str = self.dataRaw.split("\n\n")
        nodes = dict()

        for line in nodes_str.splitlines():
            nodes[line[:3]] = (line[7:10], line[12:15])

        current = "AAA"

        count = 0
        while current != "ZZZ":
            match instructions[count % len(instructions)]:
                case 'L':
                    current = nodes[current][0]
                case 'R':
                    current = nodes[current][1]

            count += 1

        return count

    def Part2(self) -> BaseSolution.ResultType:
        instructions, nodes_str = self.dataRaw.split("\n\n")
        nodes = dict()
        starts: list[str] = []

        for line in nodes_str.splitlines():
            node = line[:3]
            nodes[node] = (line[7:10], line[12:15])

            if node.endswith('A'):
                starts.append(node)

        counts = []
        for s in starts:
            current = s

            count = 0
            while not current.endswith('Z'):
                match instructions[count % len(instructions)]:
                    case 'L':
                        current = nodes[current][0]
                    case 'R':
                        current = nodes[current][1]

                count += 1

            counts.append(count)

        return math.lcm(*counts)
