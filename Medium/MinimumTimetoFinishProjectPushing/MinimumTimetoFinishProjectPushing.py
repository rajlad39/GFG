from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n

        # Build adjacency list and compute in-degrees
        for u, v in dependencies:
            adj[u].append(v)
            in_degree[v] += 1

        queue = deque()
        completion_time = list(duration)

        # Add all nodes with 0 in-degree to the queue
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)

        processed_count = 0

        # Process nodes using Kahn's algorithm
        while queue:
            u = queue.popleft()
            processed_count += 1

            for v in adj[u]:
                # Update completion time for node v
                completion_time[v] = max(completion_time[v], completion_time[u] + duration[v])

                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # If there is a cycle, not all nodes will be processed
        if processed_count != n:
            return -1

        return max(completion_time) if completion_time else 0