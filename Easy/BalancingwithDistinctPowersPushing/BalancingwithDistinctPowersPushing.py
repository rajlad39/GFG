class Solution:
    def balancePan(self, a: int, b: int) -> bool:
        while b > 0:
            rem = b % a
            if rem == 0:
                b //= a
            elif rem == 1:
                b = (b - 1) // a
            elif rem == a - 1:
                b = (b + 1) // a
            else:
                return False
        return True