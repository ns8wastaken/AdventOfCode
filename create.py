import argparse
import os
from pathlib import Path

PARSER = argparse.ArgumentParser()

PARSER.add_argument("--year", "-Y", type=int, help="Puzzle year", required=True)
PARSER.add_argument("--day",  "-D", type=int, help="Puzzle day",  required=True)

if __name__ == "__main__":
    args = PARSER.parse_args()

    rootDir = Path(__file__).parent
    yearPath = (rootDir / f"{args.year}").resolve()
    filePath = (rootDir / f"{args.year}/day{args.day:>02}.py").resolve()

    if os.path.exists(yearPath) == False:
        os.mkdir(yearPath)

    if os.path.exists(filePath) == False:
        with open(filePath, "w") as f:
            f.write("""\
from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        return NotImplemented

    def Part2(self) -> BaseSolution.ResultType:
        return NotImplemented
""")

        print(f"Created {filePath}")

    else:
        print(f"{filePath} already exists")
