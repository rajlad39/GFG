class Solution:
    def maxFrequency(self, arr: list[int], k: int) -> int:
        arr.sort()

        left = 0
        current_sum = 0
        max_freq = 0

        for right in range(len(arr)):
            current_sum += arr[right]

            # Total operations needed to make all elements in window equal to arr[right]
            # If operations required > k, shrink the window from the left
            while (right - left + 1) * arr[right] - current_sum > k:
                current_sum -= arr[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)

        return max_freq