from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        initialValues, commandsRaw = self.dataRaw.split('\n\n')
        variables = {(x := line.split(": "))[0]: int(x[1]) for line in initialValues.splitlines()}
        commands = commandsRaw.splitlines()

        orderedCommands: list[tuple[str, str, str, str]] = []
        alreadyDone = set()
        for _ in range(len(commands)):
            for line in commands:
                c, out = line.split(" -> ")
                v1, op, v2 = c.split(' ')

                tup = (v1, v2, op, out)

                if tup in alreadyDone:
                    continue

                if v1 in variables and v2 in variables:
                    orderedCommands.append(tup)
                    alreadyDone.add(tup)

                    if out not in variables:
                        variables[out] = 0

        for v1, v2, op, out in orderedCommands:
            match op:
                case "AND":
                    variables[out] = variables[v1] & variables[v2]

                case "OR":
                    variables[out] = variables[v1] | variables[v2]

                case "XOR":
                    variables[out] = variables[v1] ^ variables[v2]

        t = 0
        for i in range(100):
            z = f"z{i:>02}"

            if z not in variables:
                break

            t += variables[z] * (1 << i)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
