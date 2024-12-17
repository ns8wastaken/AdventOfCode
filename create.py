import argparse
import os
from pathlib import Path

PARSER = argparse.ArgumentParser()

PARSER.add_argument("--year", "-Y", type=int, help="Puzzle year", required=True)
PARSER.add_argument("--day",  "-D", type=int, help="Puzzle day",  required=True)

if __name__ == "__main__":
    args = PARSER.parse_args()

    filePath = Path(__file__).parent / f"{args.year}/day{args.day}.py"

    if os.path.exists(filePath) == False:
        with open(filePath, "w") as f:
            f.write("from common.base_solution import BaseSolution\n\nclass Solution(BaseSolution):\n    def Part1(self) -> None:\n        pass\n\n    def Part2(self) -> None:\n        pass\n")
