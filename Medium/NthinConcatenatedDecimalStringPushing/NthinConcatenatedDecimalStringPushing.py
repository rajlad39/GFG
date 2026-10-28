class Solution:
    def nthCharacter(self, n: int) -> str:
        d = 1
        count = 9
        start = 1

        # Step 1: Find the digit length (d) of the number containing the n-th character
        while n > d * count:
            n -= d * count
            d += 1
            count *= 10
            start *= 10

        # Step 2: Find the exact number
        num = start + (n - 1) // d

        # Step 3: Find and return the specific character
        return str(num)[(n - 1) % d]