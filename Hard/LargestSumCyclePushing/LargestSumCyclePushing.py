from typing import List

class Solution:
    def largestSumCycle(self, edge: List[int]) -> int:
        n = len(edge)
        visited = [0] * n  # 0: unvisited, 1: visiting, 2: fully visited
        max_sum = -1

        for i in range(n):
            if visited[i] == 0:
                curr = i
                path = []
                pos = {}  # Maps node -> index in the current path

                while curr != -1 and visited[curr] == 0:
                    visited[curr] = 1
                    pos[curr] = len(path)
                    path.append(curr)
                    curr = edge[curr]

                # If we hit a node currently in the visiting state, we found a cycle
                if curr != -1 and visited[curr] == 1:
                    cycle_start_idx = pos[curr]
                    cycle_nodes = path[cycle_start_idx:]
                    current_cycle_sum = sum(cycle_nodes)
                    if current_cycle_sum > max_sum:
                        max_sum = current_cycle_sum

                # Mark all nodes in the path as fully visited
                for node in path:
                    visited[node] = 2

        return max_sum