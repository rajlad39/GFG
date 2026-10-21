from typing import List

class Solution:
    def minSubarraySum(self, arr: List[int]) -> int:
        min_so_far = arr[0]
        current_min = arr[0]

        for i in range(1, len(arr)):
            current_min = min(arr[i], current_min + arr[i])
            min_so_far = min(min_so_far, current_min)

        return min_so_far