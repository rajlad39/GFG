class Solution:
    def minSquares(self, n: int, m: int) -> int:
        res = 0
        while n > 0 and m > 0:
            if n < m:
                n, m = m, n
            res += n // m
            n %= m
        return res