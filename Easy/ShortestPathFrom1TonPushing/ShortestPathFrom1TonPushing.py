class Solution:
    def minimumStep(self, n: int) -> int:
        steps = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
                steps += 1
            else:
                rem = n % 3
                if n - rem < 1:
                    steps += (n - 1)
                    n = 1
                else:
                    steps += rem
                    n -= rem
        return steps