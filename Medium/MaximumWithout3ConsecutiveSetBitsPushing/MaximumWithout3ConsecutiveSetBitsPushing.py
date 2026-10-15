class Solution:
    def maxValue(self, n: int) -> int:
        res = n
        # Check bits from the highest possible position down to 2
        for i in range(30, 1, -1):
            # Check if bits at i, i-1, and i-2 are all set (111)
            if (res & (1 << i)) and (res & (1 << (i - 1))) and (res & (1 << (i - 2))):
                # Clear the lowest bit of the three consecutive set bits
                res &= ~(1 << (i - 2))
        return res