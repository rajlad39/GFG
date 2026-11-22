class Solution:
    def longestSubarrayDivK(self, arr: list[int], k: int) -> int:
        prefix_sum = 0
        max_len = 0
        first_seen = {0: -1}

        for i, val in enumerate(arr):
            prefix_sum += val
            rem = prefix_sum % k  # Python's % always returns a value in [0, k - 1] for positive k

            if rem in first_seen:
                max_len = max(max_len, i - first_seen[rem])
            else:
                first_seen[rem] = i

        return max_len