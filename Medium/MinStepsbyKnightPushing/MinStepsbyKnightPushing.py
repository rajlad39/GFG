from collections import deque

class Solution:
    def minStepToReachTarget(self, knightPos, targetPos, n):
        # Base case: knight is already at target position
        if knightPos[0] == targetPos[0] and knightPos[1] == targetPos[1]:
            return 0

        # All 8 possible moves for a Knight
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2),  (1, 2),  (2, -1),  (2, 1)
        ]

        # 2D array to keep track of visited cells (using 1-based size)
        visited = [[False] * (n + 1) for _ in range(n + 1)]

        # Queue stores tuples of (row, col, steps)
        queue = deque([(knightPos[0], knightPos[1], 0)])
        visited[knightPos[0]][knightPos[1]] = True

        while queue:
            r, c, steps = queue.popleft()

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                # Check if target position is reached
                if nr == targetPos[0] and nc == targetPos[1]:
                    return steps + 1

                # Validate boundary constraints (1-based indexing) and check if unvisited
                if 1 <= nr <= n and 1 <= nc <= n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, steps + 1))

        return -1
        