from typing import List

class Solution:
    def minDiff(self, k: int, arr: List[int]) -> int:
        n = len(arr)
        if k == 0:
            return max(arr) - min(arr)

        # Precompute prefix max and min
        pref_max = [0] * n
        pref_min = [0] * n
        curr_max = arr[0]
        curr_min = arr[0]
        for i in range(n):
            curr_max = max(curr_max, arr[i])
            curr_min = min(curr_min, arr[i])
            pref_max[i] = curr_max
            pref_min[i] = curr_min

        # Precompute suffix max and min
        suff_max = [0] * n
        suff_min = [0] * n
        curr_max = arr[-1]
        curr_min = arr[-1]
        for i in range(n - 1, -1, -1):
            curr_max = max(curr_max, arr[i])
            curr_min = min(curr_min, arr[i])
            suff_max[i] = curr_max
            suff_min[i] = curr_min

        min_diff = float('inf')

        # Try removing every subarray of size k starting at index i
        for i in range(n - k + 1):
            rem_max = -1
            rem_min = float('inf')

            has_pref = (i > 0)
            has_suff = (i + k < n)

            if has_pref:
                rem_max = max(rem_max, pref_max[i - 1])
                rem_min = min(rem_min, pref_min[i - 1])
            if has_suff:
                rem_max = max(rem_max, suff_max[i + k])
                rem_min = min(rem_min, suff_min[i + k])

            min_diff = min(min_diff, rem_max - rem_min)

        return min_diff