from typing import List

class Solution:
    def checkWithinK(self, arr: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(arr):
            # If the number has been seen before and the distance is <= k
            if num in last_seen and i - last_seen[num] <= k:
                return True
            # Update the last seen index of the current element
            last_seen[num] = i

        return False