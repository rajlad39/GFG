class Solution:
    def minFlips(self, s: str) -> int:
        flips_start_with_zero = 0
        for i, ch in enumerate(s):
            expected = '0' if i % 2 == 0 else '1'
            if ch != expected:
                flips_start_with_zero += 1

        flips_start_with_one = len(s) - flips_start_with_zero
        return min(flips_start_with_zero, flips_start_with_one)