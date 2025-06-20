from common.base_solution import BaseSolution

def GetNextSecret(n: int) -> int:
    x = (n ^ (n * 64)) % 16777216
    k = (x ^ (x // 32)) % 16777216
    p = (k ^ (k * 2048)) % 16777216
    return p

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        data = map(int, self.dataRaw.split('\n'))
        output = []
        for i in data:
            for _ in range(2000):
                i = GetNextSecret(i)
            output.append(i)
        return sum(output)

    def Part2(self) -> BaseSolution.ResultType:
        data = list(map(int, self.dataRaw.split('\n')))

        prices: list[list[int]] = []
        diffs: list[list[int]] = []

        # Get prices
        for i, secret in enumerate(data):
            prices.append([])
            for _ in range(2000):
                prices[i].append(int(str(secret)[-1]))
                secret = GetNextSecret(secret)

        # Get price diffs
        for p in prices:
            diffs.append([])
            for i in range(1, len(p)):
                diffs[-1].append(p[i] - p[i-1])

        # Dict to store subsequences/price pairs
        # Get all subsequences of length 4
        subsequences = []
        for i, d in enumerate(diffs):
            subsequences.append(dict())
            for j in range(1, len(d) - 3):
                tup = tuple(d[j:j+4])
                if tup not in subsequences[i]:
                    subsequences[i][tup] = prices[i][j+4]

        allSequences = list(set(seq for subs in subsequences for seq in subs))

        # Get the max amount of bananas/money
        maxTotal = 0

        for seq in allSequences:
            total = 0

            for subs in subsequences:
                if seq in subs:
                    total += subs[seq]

            if total > maxTotal:
                maxTotal = total

        return maxTotal
