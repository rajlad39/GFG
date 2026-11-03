from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> int:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Number of new paths formed by merging these two components
            new_paths = self.size[root_i] * self.size[root_j]
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return new_paths
        return 0

class Solution:
    def maximumWeight(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        # Sort edges by weight
        edges.sort(key=lambda x: x[2])

        # Sort queries with their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])

        dsu = DSU(n)
        ans = [0] * len(queries)
        edge_idx = 0
        num_edges = len(edges)
        current_paths = 0

        for q_orig_idx, limit in indexed_queries:
            # Add all edges with weight <= current query limit
            while edge_idx < num_edges and edges[edge_idx][2] <= limit:
                u, v, w = edges[edge_idx]
                current_paths += dsu.union(u, v)
                edge_idx += 1

            ans[q_orig_idx] = current_paths

        return ans