from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        maps = [m.split() for m in self.dataRaw.strip().split("\n\n")]

        def reflectionize(pattern: list[str]) -> int:
            for i in range(1, len(pattern)):
                top = pattern[:i][::-1]
                bottom = pattern[i:]
                min_len = min(len(top), len(bottom))

                if top[:min_len] == bottom[:min_len]:
                    return i

            return 0

        zippy = lambda m: list(map(''.join, zip(*m)))

        t = 0

        for m in maps:
            vert = reflectionize(m)

            if vert:
                t += vert * 100

            else:
                horz = reflectionize(zippy(m))
                t += horz

        return t

    def Part2(self) -> BaseSolution.ResultType:
        maps = [
            [
                [c == '#' for c in row]
                for row in m.split()
            ] for m in self.dataRaw.strip().split("\n\n")
        ]

        def reflectionize_with_smudge(pattern: list[list[bool]]) -> int:
            for i in range(1, len(pattern)):
                top = pattern[:i][::-1]
                bottom = pattern[i:]
                min_len = min(len(top), len(bottom))

                mismatches = 0
                for a, b in zip(top[:min_len], bottom[:min_len]):
                    for x, y in zip(a, b):
                        if x != y:
                            mismatches += 1
                            if mismatches > 1:
                                break
                    if mismatches > 1:
                        break

                if mismatches == 1:
                    return i

            return 0

        zippy = lambda m: list(map(list, zip(*m)))

        t = 0

        for m in maps:
            vert = reflectionize_with_smudge(m)

            if vert:
                t += vert * 100
                continue

            horz = reflectionize_with_smudge(zippy(m))

            if horz:
                t += horz
                continue

        return t
