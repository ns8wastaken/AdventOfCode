from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            lists = line.split(": ")[1]
            winning, nums = (set(i.strip().split()) for i in lists.split(" | "))
            matches = winning & nums
            n = len(matches)
            if n > 0:
                t += 1 << (n - 1)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        card_counts = dict()

        for card, line in enumerate(self.dataRaw.splitlines()):
            lists = line.split(": ")[1]
            winning, nums = (set(i.strip().split()) for i in lists.split(" | "))
            matches = winning & nums

            if card not in card_counts:
                card_counts[card] = 1

            for i in range(card + 1, card + len(matches) + 1):
                card_counts[i] = card_counts.get(i, 1) + card_counts[card]

        return sum(card_counts.values())
