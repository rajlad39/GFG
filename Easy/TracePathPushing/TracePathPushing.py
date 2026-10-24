class Solution:
    def isPossible(self, n: int, m: int, s: str) -> bool:
        curr_r = 0
        curr_c = 0
        min_r = max_r = 0
        min_c = max_c = 0

        # Track relative displacements
        for char in s:
            if char == 'L':
                curr_c -= 1
            elif char == 'R':
                curr_c += 1
            elif char == 'D':
                curr_r -= 1
            elif char == 'U':
                curr_r += 1

            min_r = min(min_r, curr_r)
            max_r = max(max_r, curr_r)
            min_c = min(min_c, curr_c)
            max_c = max(max_c, curr_c)

        # Check if there's a valid starting row and column range
        row_valid = (-min_r <= n - 1 - max_r)
        col_valid = (-min_c <= m - 1 - max_c)

        return row_valid and col_valid