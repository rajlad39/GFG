class Solution:
    def update(self, n: int, updates: list[int]) -> None:
        # Code here
        arr = [0] * n
        for j in updates:
            arr[j - 1] += 1

        current_sum = 0
        for i in range(n):
            current_sum += arr[i]
            arr[i] = current_sum

        # If the platform expects modifications in-place, copy back
        # or return the array if it expects a return value:
        # (Depending on GFG signature variant, returning arr or modifying in place)
        return arr