class Solution:
    def findKthSmall(self, arr: list[int], k: int) -> int:
        arr.sort()
        n = len(arr)

        for i in range(n):
            if arr[i] - (i + 1) >= k:
                return k + i

        return k + n