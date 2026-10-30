from typing import List

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        limit = max(max(arr), r) + 2
        cnt = [0] * limit
        for x in arr:
            if x < limit:
                cnt[x] += 1

        # Precompute powers of 2 modulo MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        # F[v] = (2^cnt[v] - 1) % MOD
        F = [0] * limit
        for v in range(limit):
            F[v] = (pow2[cnt[v]] - 1) % MOD

        # Prefix products: PP[X] = product of F[v] for v from 0 to X-1
        PP = [1] * (limit + 1)
        for X in range(1, limit + 1):
            PP[X] = (PP[X - 1] * F[X - 1]) % MOD

        # Prefix sums of counts: CS[X] = sum of cnt[v] for v from 0 to X
        CS = [0] * limit
        CS[0] = cnt[0]
        for v in range(1, limit):
            CS[v] = CS[v - 1] + cnt[v]

        total_subsets = 0
        for X in range(l, r + 1):
            cs_val = CS[X] if X < limit else n
            rem_cnt = n - cs_val
            S_X = pow2[rem_cnt] if 0 <= rem_cnt <= n else 1
            P_X = PP[X]

            ans_X = (P_X * S_X) % MOD
            total_subsets = (total_subsets + ans_X) % MOD

        return total_subsets