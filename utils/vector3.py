class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_iter(cls, iterable) -> "Vec3":
        x, y, z = iterable
        return cls(float(x), float(y), float(z))

    def copy(self):
        return Vec3(self.x, self.y, self.z)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vec3):
            return NotImplemented
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __add__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __iadd__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            self.x += other.x
            self.y += other.y
            self.z += other.z
        else:
            self.x += other
            self.y += other
            self.z += other

        return self

    def __sub__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Vec3(self.x - other, self.y - other, self.z - other)

    def __isub__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        else:
            self.x -= other
            self.y -= other
            self.z -= other

        return self

    def __mul__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __imul__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            self.x *= other.x
            self.y *= other.y
            self.z *= other.z
        else:
            self.x *= other
            self.y *= other
            self.z *= other

        return self

    def __truediv__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            return Vec3(self.x / other, self.y / other, self.z / other)

    def __itruediv__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            self.x /= other.x
            self.y /= other.y
            self.z /= other.z
        else:
            self.x /= other
            self.y /= other
            self.z /= other

        return self

    def __floordiv__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            return Vec3(self.x // other.x, self.y // other.y, self.z // other.z)
        else:
            return Vec3(self.x // other, self.y // other, self.z // other)

    def __ifloordiv__(self, other: "Vec3 | float") -> "Vec3":
        if isinstance(other, Vec3):
            self.x //= other.x
            self.y //= other.y
            self.z //= other.z
        else:
            self.x //= other
            self.y //= other
            self.z //= other

        return self

    def __neg__(self) -> "Vec3":
        return Vec3(-self.x, -self.y, -self.z)

    def dist(self, other: "Vec3") -> float:
        return (
            (self.x - other.x) ** 2
            + (self.y - other.y) ** 2
            + (self.z - other.z) ** 2
        ) ** 0.5
