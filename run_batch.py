import argparse
import os
from pathlib import Path

PARSER = argparse.ArgumentParser()

PARSER.add_argument("--session", "-S", type=str, help="Session key", required=False)
PARSER.add_argument("--year",    "-Y", type=int, help="Puzzle year", required=True)

if __name__ == "__main__":
    args = PARSER.parse_args()

    # How to find your session key (on firefox at least):
    # 1) Go to any advent of code problem page such as https://adventofcode.com/2021/day/1
    # 2) Inspect element -> Storage tab -> Cookies
    # 3) Get the value of the "session" key and paste it after the --session argument in the commandline
    # THE SESSION KEY WILL BE SAVED IN "session_key.txt" WHENEVER IT IS PROVIDED

    sessionKeyFilePath = Path(__file__).parent / "session_key.txt"
    sessionKey = ""

    if args.session == None:
        if os.path.exists(sessionKeyFilePath):
            with open(sessionKeyFilePath, "r") as f:
                sessionKey = f.read().strip()

        else:
            raise RuntimeError("There is no session_key.txt file and the session key was not provided")

    else:
        with open(sessionKeyFilePath, "w") as f:
            f.write(args.session)
        sessionKey = args.session

    print(f"┼{"─" * 17}┼{"─" * 28}┼{"─" * 27}┼")
    print(f"│      Year       │    Results for part 1      │    Results for part 2     │")

    baseFilePath = Path(__file__).parent / str(args.year)
    for file in sorted([i for i in os.listdir(baseFilePath) if i.endswith(".py")], key=lambda i: int(i.split(".")[0][3:])):
        filePath = baseFilePath / file

        day = int(filePath.name.split(".")[0][3:])
        solution = __import__(f"{args.year}.day{day:>02}", fromlist=["Solution"]).Solution(args.year, day, sessionKey)

        print(f"┼{"─" * 17}┼{"─" * 28}┼{"─" * 27}┼")
        print(f"│Year {args.year} Day {str(day).rjust(2, "0")} │ Part 1: {str(solution.Part1()).rjust(18)} │ Part 2: {str(solution.Part2()).rjust(18)}│")

    print(f"┼{"─" * 17}┼{"─" * 28}┼{"─" * 27}┼")
    print()
