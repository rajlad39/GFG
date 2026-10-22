class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        X = []

        # Build the sequence X for the first half + middle
        for i in range(n // 2):
            c1 = s[i]
            c2 = s[n - 1 - i]
            if c1 != '?' and c2 != '?':
                if c1 != c2:
                    return -1
                X.append(ord(c1) - ord('a'))
            elif c1 != '?' and c2 == '?':
                X.append(ord(c1) - ord('a'))
            elif c1 == '?' and c2 != '?':
                X.append(ord(c2) - ord('a'))
            else:
                X.append(None)

        if n % 2 == 1:
            mid = n // 2
            c = s[mid]
            if c != '?':
                X.append(ord(c) - ord('a'))
            else:
                X.append(None)

        L = len(X)
        if L == 0:
            return 0

        Sigma = 26

        # Initialize DP for the first element
        if X[0] is not None:
            dp = [float('inf')] * Sigma
            dp[X[0]] = 0
        else:
            dp = [0] * Sigma

        def get_next_dp(curr_dp):
            pref = [float('inf')] * Sigma
            cur_min = float('inf')
            for p in range(Sigma):
                cur_min = min(cur_min, curr_dp[p] - p)
                pref[p] = cur_min

            suff = [float('inf')] * Sigma
            cur_min = float('inf')
            for p in range(Sigma - 1, -1, -1):
                cur_min = min(cur_min, curr_dp[p] + p)
                suff[p] = cur_min

            g = [float('inf')] * Sigma
            for c in range(Sigma):
                val1 = c + pref[c]
                val2 = -c + (suff[c+1] if c + 1 < Sigma else float('inf'))
                g[c] = min(val1, val2)
            return g

        # Process remaining elements using DP transitions
        for j in range(1, L):
            g = get_next_dp(dp)
            new_dp = [float('inf')] * Sigma
            if X[j] is not None:
                new_dp[X[j]] = g[X[j]]
            else:
                new_dp = g
            dp = new_dp

        min_total_cost = min(dp)
        if min_total_cost == float('inf'):
            return -1

        return 2 * min_total_cost