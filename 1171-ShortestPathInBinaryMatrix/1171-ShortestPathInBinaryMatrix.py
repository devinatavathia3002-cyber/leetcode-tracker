# Last updated: 2/9/2026, 9:54:10 PM
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),     # up, down, left, right
            (-1, -1), (-1, 1), (1, -1), (1, 1)    # 4 diagonals
        ]

        queue = deque()
        queue.append((0, 0, 1))  # (row, col, path_length)
        visited = set()
        visited.add((0, 0))

        while queue:
            x, y, path = queue.popleft()

            if x == ROWS - 1 and y == COLS - 1:
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (
                    0 <= nx < ROWS and
                    0 <= ny < COLS and
                    grid[nx][ny] == 0 and
                    (nx, ny) not in visited
                ):
                    queue.append((nx, ny, path + 1))
                    visited.add((nx, ny))

        return -1
