l1 = []
l2 = []

with open("data1.txt", "r") as f:
    for i in f.readlines():
        l1.append(int(i[:5]))
        l2.append(int(i[8:]))

l1.sort()
l2.sort()

total = 0

for i in range(len(l1)):
    total += abs(l1[i] - l2[i])

print(total)
