from typing import List

class Solution:
    def goodIndices(self, arr: List[int]) -> int:
        n = len(arr)
        state = [0] * n  # 0: unvisited, 1: visiting, 2: good, 3: bad

        for i in range(n):
            if state[i] != 0:
                continue

            curr = i
            path = []

            # Traverse until we hit an already visited node, out of bounds, or 0
            while 0 <= curr < n and state[curr] == 0 and arr[curr] != 0:
                state[curr] = 1
                path.append(curr)
                curr = curr + arr[curr]

            # Determine the outcome of the path
            if curr < 0 or curr >= n:
                res = 2  # Good (leads outside)
            elif state[curr] == 2:
                res = 2  # Good
            elif state[curr] == 3:
                res = 3  # Bad
            elif 0 <= curr < n and arr[curr] == 0:
                res = 3  # Bad (dead end at 0)
                state[curr] = 3
            elif state[curr] == 1:
                res = 3  # Bad (cycle detected)
            else:
                res = 3

            # Propagate the result to all nodes in the current path
            for node in path:
                state[node] = res

        # Count all nodes marked as good
        return sum(1 for x in state if x == 2)