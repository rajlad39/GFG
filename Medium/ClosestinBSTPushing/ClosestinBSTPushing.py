class Solution:
    def minDiff(self, root, k: int) -> int:
        min_diff = float('inf')
        curr = root

        while curr:
            diff = abs(curr.data - k)
            min_diff = min(min_diff, diff)

            if min_diff == 0:
                return 0

            if k < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return min_diff