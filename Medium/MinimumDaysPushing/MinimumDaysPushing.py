from typing import List

class Solution:
    def getMinimumDays(self, s: str, p: List[int]) -> int:
        n = len(s)

        # Helper function to check if the condition is met after 'days'
        def isValid(days: int) -> bool:
            arr = list(s)
            for i in range(days):
                arr[p[i]] = '?'

            # Check adjacent non-'?' elements
            for i in range(n - 1):
                if arr[i] != '?' and arr[i + 1] != '?' and arr[i] == arr[i + 1]:
                    return False
            return True

        # Binary search over the number of days [0, n]
        low, high = 0, n
        ans = n

        while low <= high:
            mid = (low + high) // 2
            if isValid(mid):
                ans = mid
                high = mid - 1  # Try to find a smaller valid day count
            else:
                low = mid + 1   # Need more days

        return ans