from typing import Callable, TypeVar

T = TypeVar("T")

def str2mat(s: str, _map: Callable[[str], T] = lambda x: x) -> list[list[T]]:
    return [[_map(ch) for ch in line] for line in s.splitlines()]
