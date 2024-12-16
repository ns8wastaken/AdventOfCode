from abc import abstractmethod
from typing import Any
import requests

class BaseSolution:
    def __init__(self, year: int, day: int, sessionKey: str):
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        response = requests.get(url, cookies={"session": sessionKey})

        # Handle request errors
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch input: {response.status_code} {response.reason}")

        self.dataRaw = response.text.strip()

    @abstractmethod
    def Part1(self) -> Any:
        """Solve Part 1 of the problem."""
        pass

    @abstractmethod
    def Part2(self) -> Any:
        """Solve Part 2 of the problem."""
        pass