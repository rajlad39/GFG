class Solution:
    def findMinCost(self, s1: str, s2: str, costS1: int, costS2: int) -> int:
        m, n = len(s1), len(s2)

        # dp[i][j] stores the length of the LCS of s1[:i] and s2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_len = dp[m][n]

        # Calculate minimum cost
        total_cost = (m * costS1) + (n * costS2) - lcs_len * (costS1 + costS2)
        return total_cost