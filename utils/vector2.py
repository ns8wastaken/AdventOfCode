class Vec2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vec2):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            return Vec2(self.x + other, self.y + other)

    def __iadd__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

        return self

    def __sub__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __isub__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

        return self

    def __mul__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            return Vec2(self.x * other.x, self.y * other.y)
        else:
            return Vec2(self.x * other, self.y * other)

    def __imul__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other

        return self

    def __truediv__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            return Vec2(self.x / other.x, self.y / other.y)
        else:
            return Vec2(self.x / other, self.y / other)

    def __itruediv__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other

        return self

    def __floordiv__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            return Vec2(self.x // other.x, self.y // other.y)
        else:
            return Vec2(self.x // other, self.y // other)

    def __ifloordiv__(self, other: "Vec2 | float") -> "Vec2":
        if isinstance(other, Vec2):
            self.x //= other.x
            self.y //= other.y
        else:
            self.x //= other
            self.y //= other

        return self
