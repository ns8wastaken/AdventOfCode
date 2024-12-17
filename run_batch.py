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

    for file in [i for i in os.listdir(str(args.year)) if i.endswith(".py")]:
        filePath = Path(__file__).parent / str(args.year) / file

        day = int(filePath.name.split(".")[0][3:])

        print(f"Results for year {args.year}, day {day}:")

        solution = __import__(f"{args.year}.day{day}", fromlist=["Solution"]).Solution(args.year, day, sessionKey)
        print("Part 1:", solution.Part1())
        print("Part 2:", solution.Part2())
        print()
