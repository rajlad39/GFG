from typing import List

class Solution:
    def lexicographicallyLargest(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0

        while i < n:
            j = i
            # Find the contiguous segment with the same parity
            while j < n and (arr[j] % 2 == arr[i] % 2):
                j += 1

            # Extract, sort in descending order, and place back
            segment = arr[i:j]
            segment.sort(reverse=True)
            arr[i:j] = segment

            i = j

        return arr