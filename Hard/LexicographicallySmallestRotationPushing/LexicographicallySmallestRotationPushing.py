class Solution:
    def lexiString(self, s: str) -> str:
        n = len(s)
        s_double = s + s

        i, j = 0, 1
        while i < n and j < n:
            k = 0
            while k < n and s_double[i + k] == s_double[j + k]:
                k += 1

            if k == n:
                break

            if s_double[i + k] > s_double[j + k]:
                i = max(i + k + 1, j + 1)
            else:
                j = max(j + k + 1, i + 1)

            if i == j:
                j += 1

        start_idx = min(i, j)
        return s_double[start_idx : start_idx + n]