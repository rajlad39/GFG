class Solution:
    def minTime(self, n: int, s1: int, s2: int) -> int:
        low = 0
        high = min(s1, s2) * n
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Total documents scanned by both scanners in 'mid' units of time
            docs_scanned = (mid // s1) + (mid // s2)

            if docs_scanned >= n:
                ans = mid
                high = mid - 1  # Try to find a smaller valid time
            else:
                low = mid + 1   # Need more time

        return ans