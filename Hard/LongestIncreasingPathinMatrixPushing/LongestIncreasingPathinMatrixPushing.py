class Solution:
    def longIncPath(self, mat: list[list[int]], n: int, m: int) -> int:
        if not mat or not mat[0]:
            return 0

        # memo[i][j] stores the length of the longest increasing path starting at (i, j)
        memo = [[0] * m for _ in range(n)]

        def dfs(r, c):
            if memo[r][c] != 0:
                return memo[r][c]

            max_len = 1

            # Explore 4 directional moves: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] > mat[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[r][c] = max_len
            return memo[r][c]

        longest_path = 0
        for i in range(n):
            for j in range(m):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path