from collections import defaultdict


class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        n = len(arr)
        pair_map = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                pair_map[arr[i] + arr[j]].append((i, j))

        best = None

        for pairs in pair_map.values():
            m = len(pairs)
            for x in range(m):
                a, b = pairs[x]
                if best is not None and (a, b) > (best[0], best[1]):
                    break

                for y in range(x + 1, m):
                    c, d = pairs[y]
                    if a != c and a != d and b != c and b != d:
                        cand = (a, b, c, d)
                        if best is None or cand < best:
                            best = cand
                        break

        return list(best) if best is not None else [-1, -1, -1, -1]