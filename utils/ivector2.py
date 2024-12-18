class IVec2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IVec2):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            return IVec2(self.x + other.x, self.y + other.y)
        else:
            return IVec2(self.x + other, self.y + other)

    def __iadd__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

        return self

    def __sub__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            return IVec2(self.x - other.x, self.y - other.y)
        else:
            return IVec2(self.x - other, self.y - other)

    def __isub__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other

        return self

    def __mul__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            return IVec2(self.x * other.x, self.y * other.y)
        else:
            return IVec2(self.x * other, self.y * other)

    def __imul__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other

        return self

    def __truediv__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            return IVec2(self.x // other.x, self.y // other.y)
        else:
            return IVec2(self.x // other, self.y // other)

    def __itruediv__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            self.x //= other.x
            self.y //= other.y
        else:
            self.x //= other
            self.y //= other

        return self

    def __floordiv__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            return IVec2(self.x // other.x, self.y // other.y)
        else:
            return IVec2(self.x // other, self.y // other)

    def __ifloordiv__(self, other: "IVec2 | int") -> "IVec2":
        if isinstance(other, IVec2):
            self.x //= other.x
            self.y //= other.y
        else:
            self.x //= other
            self.y //= other

        return self