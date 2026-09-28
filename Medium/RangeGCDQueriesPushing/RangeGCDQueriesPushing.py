import math

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        n = len(arr)

        # Segment tree array
        tree = [0] * (4 * n)

        # Build segment tree
        def build(node, start, end):
            if start == end:
                tree[node] = arr[start]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = math.gcd(tree[2 * node], tree[2 * node + 1])

        # Point update: arr[idx] = val
        def update(node, start, end, idx, val):
            if start == end:
                tree[node] = val
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, end, idx, val)
            tree[node] = math.gcd(tree[2 * node], tree[2 * node + 1])

        # Range query: GCD in [l, r]
        def query_gcd(node, start, end, l, r):
            if r < start or end < l:
                return 0  # gcd(x, 0) = x
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            left_gcd = query_gcd(2 * node, start, mid, l, r)
            right_gcd = query_gcd(2 * node + 1, mid + 1, end, l, r)
            return math.gcd(left_gcd, right_gcd)

        # Initialize segment tree
        build(1, 0, n - 1)

        result = []
        for q in queries:
            if q[0] == 0:
                # Type 1: [0, l, r]
                result.append(query_gcd(1, 0, n - 1, q[1], q[2]))
            else:
                # Type 2: [1, index, value]
                update(1, 0, n - 1, q[1], q[2])

        return result