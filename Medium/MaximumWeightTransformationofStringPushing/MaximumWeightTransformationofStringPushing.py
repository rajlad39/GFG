class Solution:
    def getMaxWeight(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1

        # Assign weights to each adjacent pair (edge)
        w = [2 if s[i] != s[i+1] else 1 for i in range(n - 1)]

        # DP to find the maximum weight independent set of edges
        dp0 = 0
        dp1 = w[0]

        for i in range(1, n - 1):
            curr = max(dp1, w[i] + dp0)
            dp0 = dp1
            dp1 = curr

        return n + dp1