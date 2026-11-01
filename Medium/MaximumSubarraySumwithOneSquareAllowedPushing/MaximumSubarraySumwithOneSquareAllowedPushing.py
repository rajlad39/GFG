from typing import List

class Solution:
    def maximumSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 0:
            return 0

        # Initialize DP states with the first element
        dp_no_square = arr[0]
        dp_squared = arr[0] ** 2

        max_sum = max(dp_no_square, dp_squared)

        for i in range(1, n):
            val = arr[i]
            val_sq = val ** 2

            # Order matters: calculate new_dp_squared before updating dp_no_square
            new_dp_squared = max(val_sq, dp_no_square + val_sq, dp_squared + val)
            new_dp_no_square = max(val, dp_no_square + val)

            dp_squared = new_dp_squared
            dp_no_square = new_dp_no_square

            max_sum = max(max_sum, dp_squared, dp_no_square)

        return max_sum