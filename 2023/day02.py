from common.base_solution import BaseSolution

class Solution(BaseSolution):
    def Part1(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            p1, p2 = line.split(": ")
            id = p1.split(' ')[1]

            gucci = True

            for i in p2.split("; "):
                d = {
                    'red':   0,
                    'green': 0,
                    'blue':  0
                }

                for j in i.split(", "):
                    n, color = j.split(' ')
                    d[color] += int(n)

                if d['red'] > 12 or d['green'] > 13 or d['blue'] > 14:
                    gucci = False
                    break

            if gucci:
                t += int(id)

        return t

    def Part2(self) -> BaseSolution.ResultType:
        t = 0

        for line in self.dataRaw.splitlines():
            games = line.split(": ")[1]

            red = 0
            green = 0
            blue = 0

            for i in games.split("; "):
                d = {
                    'red':   0,
                    'green': 0,
                    'blue':  0
                }

                for j in i.split(", "):
                    n, color = j.split(' ')
                    d[color] += int(n)

                red   = max(red,   d['red'])
                green = max(green, d['green'])
                blue  = max(blue,  d['blue'])

            t += red * green * blue

        return t
