from typing import List

class Solution:
    def subarrayXor(self, arr: List[int]) -> int:
        n = len(arr)

        # If the length of the array is even, all elements appear an even number of times
        if n % 2 == 0:
            return 0

        # If n is odd, XOR all elements at even indices
        ans = 0
        for i in range(0, n, 2):
            ans ^= arr[i]

        return ans