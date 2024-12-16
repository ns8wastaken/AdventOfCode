import argparse

PARSER = argparse.ArgumentParser()

PARSER.add_argument("--session",  type=str, help="Session key", required=True)
PARSER.add_argument("--year",     type=int, help="Puzzle year", required=True)
PARSER.add_argument("--day",      type=int, help="Puzzle day",  required=True)

if __name__ == "__main__":
    args = PARSER.parse_args()
    print(f"Results for year {args.year}, day {args.day}:")

    # How to find your session key (on firefox at least):
    # 1) Go to any advent of code problem page such as https://adventofcode.com/2021/day/1
    # 2) Inspect element -> Storage tab -> Cookies
    # 3) Get the value of the "session" key and paste it here

    solution = __import__(f"{args.year}.day{args.day}", fromlist=["Solution"]).Solution(args.year, args.day, args.session)
    print("Part 1:", solution.Part1())
    print("Part 2:", solution.Part2())
