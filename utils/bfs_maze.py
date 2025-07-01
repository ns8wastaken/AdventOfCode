from collections import deque

def BFSMaze(
    mazeSize: tuple[int, int],
    walls:    set[tuple[int, int]],
    start:    tuple[int, int],
    end:      tuple[int, int],
    orthogonalNeighbors: bool = True,
) -> list[tuple[int, int]]:
    visited: dict[tuple[int, int], tuple[int, int] | None] = { start: None }
    queue = deque([start])

    isInMaze = lambda pos: (0 <= pos[0] < (mazeSize[0] - 1)) and (0 <= pos[1] < (mazeSize[1] - 1))

    if orthogonalNeighbors:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    else:
        dirs = (
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1)
        )

    while queue:
        current = queue.pop()

        if current == end:
            break

        for dx, dy in dirs:
            newPos = (current[0] + dx, current[1] + dy)

            if (newPos in visited) or (newPos in walls) or not isInMaze(newPos):
                continue

            visited[newPos] = current
            queue.appendleft(newPos)

    if end not in visited:
        return []

    # Reconstruct path
    path = [end]
    while (current := visited[path[-1]]) != None:
        path.append(current)

    path.reverse()
    return path
