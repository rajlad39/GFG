import sys
# Increase recursion depth for deep tree structures
sys.setrecursionlimit(200000)

class Solution:
    def longestPath(self, s: str, edges: list[list[int]]) -> int:
        n = len(s)
        if n == 0:
            return 0

        # Build adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        max_down = [0] * (n + 1)
        max_from_node = [0] * (n + 1)
        visited = [False] * (n + 1)

        # DFS 1: Calculate longest down-path within the same color component
        def dfs1(u, p):
            max_down[u] = 1
            for v in adj[u]:
                if v != p and s[v - 1] == s[u - 1]:
                    dfs1(v, u)
                    max_down[u] = max(max_down[u], 1 + max_down[v])

        # DFS 2: Rerooting DP to find maximum path length from node u within its component
        def dfs2(u, p, up_len):
            max_from_node[u] = max(max_down[u], 1 + up_len)

            # Find top 2 maximum down lengths among same-colored children
            max1, max2 = 0, 0
            for v in adj[u]:
                if v != p and s[v - 1] == s[u - 1]:
                    if max_down[v] > max1:
                        max2 = max1
                        max1 = max_down[v]
                    elif max_down[v] > max2:
                        max2 = max_down[v]

            for v in adj[u]:
                if v != p and s[v - 1] == s[u - 1]:
                    best_child = max2 if max_down[v] == max1 else max1
                    current_up = max(up_len, best_child) + 1
                    dfs2(v, u, current_up)

        # Process each same-color connected component
        for i in range(1, n + 1):
            if not visited[i]:
                # Collect connected component of the same color
                q = [i]
                visited[i] = True
                head = 0
                while head < len(q):
                    curr = q[head]
                    head += 1
                    for nxt in adj[curr]:
                        if not visited[nxt] and s[nxt - 1] == s[curr - 1]:
                            visited[nxt] = True
                            q.append(nxt)

                # Compute tree DP for this component
                dfs1(i, 0)
                dfs2(i, 0, 0)

        # 1. Purely monochromatic maximum path
        ans = max(max_from_node) if n > 0 else 0

        # 2. Transition path: Red path ending at u + Blue path starting at v
        for u, v in edges:
            if s[u - 1] != s[v - 1]:
                r_node = u if s[u - 1] == 'R' else v
                b_node = u if s[u - 1] == 'B' else v

                ans = max(ans, max_from_node[r_node] + max_from_node[b_node])

        return ans