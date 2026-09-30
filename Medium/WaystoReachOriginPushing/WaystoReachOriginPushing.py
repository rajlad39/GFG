class Solution:
    def ways(self, x: int, y: int) -> int:
        MOD = 10**9 + 7

        n = x + y
        r = min(x, y)

        num = 1
        den = 1

        for i in range(1, r + 1):
            num = (num * (n - i + 1)) % MOD
            den = (den * i) % MOD

        return (num * pow(den, MOD - 2, MOD)) % MOD