from typing import List

class Solution:
    def maxPackages(self, arr: List[int], totalTime: int) -> int:
        n = len(arr)
        if totalTime >= n:
            return sum(arr)

        # Compute the sum of the first window of size totalTime
        current_sum = sum(arr[:totalTime])
        max_packages = current_sum

        # Slide the window across the rest of the array
        for i in range(totalTime, n):
            current_sum += arr[i] - arr[i - totalTime]
            if current_sum > max_packages:
                max_packages = current_sum

        return max_packages