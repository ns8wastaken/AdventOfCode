class IVec3:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_iter(cls, iterable) -> "IVec3":
        x, y, z = iterable
        return cls(int(x), int(y), int(z))

    def copy(self):
        return IVec3(self.x, self.y, self.z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, IVec3):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __add__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            return IVec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return IVec3(self.x + other, self.y + other, self.z + other)

    def __iadd__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            self.x += other
            self.y += other
            self.z += other

        return self

    def __sub__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            return IVec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return IVec3(self.x - other, self.y - other, self.z - other)

    def __isub__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            self.x -= other
            self.y -= other
            self.z -= other

        return self

    def __mul__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            return IVec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return IVec3(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            self.x *= other
            self.y *= other
            self.z *= other

        return self

    # def __truediv__(self, other: "IVec3 | int") -> "IVec3":
    #     if isinstance(other, IVec3):
    #         return IVec3(self.x / other.x, self.y / other.y, self.z / other.z)
    #     else:
    #         return IVec3(self.x / other, self.y / other, self.z / other)
    #
    # def __itruediv__(self, other: "IVec3 | int") -> "IVec3":
    #     if isinstance(other, IVec3):
    #         self.x /= other.x
    #         self.y /= other.y
    #         self.z /= other.z
    #     else:
    #         self.x /= other
    #         self.y /= other
    #         self.z /= other
    #
    #     return self

    def __floordiv__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            return IVec3(self.x // other.x, self.y // other.y, self.z // other.z)
        else:
            return IVec3(self.x // other, self.y // other, self.z // other)

    def __ifloordiv__(self, other: "IVec3 | int") -> "IVec3":
        if isinstance(other, IVec3):
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z
        else:
            self.x //= other
            self.y //= other
            self.z //= other

        return self

    def __neg__(self) -> "IVec3":
        return IVec3(-self.x, -self.y, -self.z)

    def dist(self, other: "IVec3") -> float:
        return (
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        ) ** 0.5
