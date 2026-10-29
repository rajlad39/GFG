import heapq
from typing import List

class Solution:
    def minComputation(self, files: List[int]) -> int:
        if not files:
            return 0

        # Convert the list into a min-heap
        heapq.heapify(files)
        total_cost = 0

        while len(files) > 1:
            # Extract the two smallest files
            first = heapq.heappop(files)
            second = heapq.heappop(files)

            # Merge cost
            cost = first + second
            total_cost += cost

            # Push the combined file back into the heap
            heapq.heappush(files, cost)

        return total_cost