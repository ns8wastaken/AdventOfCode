import argparse
import os

PARSER = argparse.ArgumentParser()

PARSER.add_argument("--session",  type=str, help="Session key", required=False)
PARSER.add_argument("--year",     type=int, help="Puzzle year", required=True)
PARSER.add_argument("--day",      type=int, help="Puzzle day",  required=True)

if __name__ == "__main__":
    args = PARSER.parse_args()
    print(f"Results for year {args.year}, day {args.day}:")

    sessionKey = ""

    if args.session == None:
        if os.path.exists("session_key.txt") == False:
            raise RuntimeError("There is no session_key.txt file and the session key was not provided")

        else:
            with open("session_key.txt", "r") as f:
                sessionKey = f.read().strip()

    else:
        with open("session_key.txt", "w") as f:
            f.write(args.session)
        sessionKey = args.session


    # How to find your session key (on firefox at least):
    # 1) Go to any advent of code problem page such as https://adventofcode.com/2021/day/1
    # 2) Inspect element -> Storage tab -> Cookies
    # 3) Get the value of the "session" key and paste it after the --session argument in the commandline
    # THE SESSION KEY WILL BE SAVED IN "session_key.txt" AFTER THE FIRST TIME

    solution = __import__(f"{args.year}.day{args.day}", fromlist=["Solution"]).Solution(args.year, args.day, sessionKey)
    print("Part 1:", solution.Part1())
    print("Part 2:", solution.Part2())
