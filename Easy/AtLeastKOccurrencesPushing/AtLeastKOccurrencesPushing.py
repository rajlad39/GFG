from typing import List
from collections import defaultdict

class Solution:
    def firstElementKTime(self, arr: List[int], k: int) -> int:
        counts = defaultdict(int)

        for num in arr:
            counts[num] += 1
            if counts[num] == k:
                return num

        return -1