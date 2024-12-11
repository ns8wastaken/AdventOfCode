import re

data = ""

with open("data3.txt", "r") as f:
    data = f.read()

# total = 0

# for match in re.findall(r"mul\(\d+,\d+\)", data):
#     n1, n2 = map(int, re.findall(r"\d+", match))
#     total += n1 * n2

# print(total)

total = 0

do = True
for match in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
    if match == "do()":
        do = True

    elif match == "don't()":
        do = False

    elif do:
        n1, n2 = map(int, re.findall(r"\d+", match))
        total += n1 * n2

print(total)
