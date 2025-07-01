from common.base_solution import BaseSolution
from collections import Counter

def get_strength(hand: str) -> int:
    counts = sorted(Counter(hand).values(), reverse=True)

    match counts:
        case [5]:             return 6  # Five of a kind
        case [4, 1]:          return 5  # Four of a kind
        case [3, 2]:          return 4  # Full house
        case [3, 1, 1]:       return 3  # Three of a kind
        case [2, 2, 1]:       return 2  # Two pair
        case [2, 1, 1, 1]:    return 1  # One pair
        case [1, 1, 1, 1, 1]: return 0  # High card

    return -99999999999999999999999999999

def get_strength_with_jokers(hand: str) -> int:
    # Count each card, but don't include 'J'
    counts = Counter(c for c in hand if c != 'J')
    jokers = hand.count('J')

    if not counts:
        return 6

    freq = sorted(counts.values(), reverse=True)

    freq[0] += jokers
    freq = sorted(freq, reverse=True)

    match freq:
        case [5]: return 6  # Five of a kind
        case [4, 1]: return 5  # Four of a kind
        case [3, 2]: return 4  # Full house
        case [3, 1, 1]: return 3  # Three of a kind
        case [2, 2, 1]: return 2  # Two pair
        case [2, 1, 1, 1]: return 1  # One pair
        case [1, 1, 1, 1, 1]: return 0  # High card

    return -99999999999999999999999999999

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        hands_by_strength: list[list[tuple[str, int]]] = [
            [], [], [], [], [], [], []
        ]

        for line in self.dataRaw.splitlines():
            hand, bid = line.split()
            hands_by_strength[get_strength(hand)].append((hand, int(bid)))

        card_nums = {
            '2': 0, '3': 1, '4': 2, '5': 3,
            '6': 4, '7': 5, '8': 6, '9': 7,
            'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
        }

        t = 0

        start_rank = 1
        for hands in hands_by_strength:
            hands.sort(key=lambda c: [card_nums[ch] for ch in c[0]])

            for j, h in enumerate(hands):
                t += (start_rank + j) * h[1]

            start_rank += len(hands)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        hands_by_strength: list[list[tuple[str, int]]] = [
            [], [], [], [], [], [], []
        ]

        for line in self.dataRaw.splitlines():
            hand, bid = line.split()
            hands_by_strength[get_strength_with_jokers(hand)].append((hand, int(bid)))

        card_nums = {
            'J': 0, '2': 1, '3': 2, '4': 3, '5': 4,
            '6': 5, '7': 6, '8': 7, '9': 8,
            'T': 9, 'Q': 10, 'K': 11, 'A': 12
        }

        t = 0

        start_rank = 1
        for hands in hands_by_strength:
            hands.sort(key=lambda c: [card_nums[ch] for ch in c[0]])

            for j, h in enumerate(hands):
                t += (start_rank + j) * h[1]

            start_rank += len(hands)

        return t
