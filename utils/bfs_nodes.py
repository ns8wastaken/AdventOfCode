from collections import deque
from typing import Any

def BFSNodes(
    nodes: dict[Any, Any],
    start: Any,
    end:   Any
) -> list[tuple[int, int]]:
    visited: dict[
        tuple[int, int],
        tuple[int, int] | None
    ] = { start: None }
    queue = deque([start])

    while queue:
        current = queue.pop()

        if current == end:
            break

        for neighbor in nodes[current]:
            if neighbor in visited:
                continue

            visited[neighbor] = current
            queue.appendleft(neighbor)

    if end not in visited:
        return []

    # Reconstruct path
    path = [end]
    while (current := visited[path[-1]]) != None:
        path.append(current)

    path.reverse()
    return path
