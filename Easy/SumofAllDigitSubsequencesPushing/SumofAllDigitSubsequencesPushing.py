class Solution:
    def subsequenceSum(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # Sum of all digits in the string modulo 10^9 + 7
        digit_sum = sum(int(c) for c in s) % MOD

        # Each digit appears 2^(n-1) times in the subsequences
        multiplier = pow(2, n - 1, MOD)

        return (digit_sum * multiplier) % MOD