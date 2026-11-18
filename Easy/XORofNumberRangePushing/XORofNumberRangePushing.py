class Solution:
    def computeXOR(self, n: int) -> int:
        if n < 0:
            return 0
        rem = n % 4
        if rem == 0:
            return n
        elif rem == 1:
            return 1
        elif rem == 2:
            return n + 1
        else:
            return 0

    def findXOR(self, l: int, r: int) -> int:
        return self.computeXOR(l - 1) ^ self.computeXOR(r)