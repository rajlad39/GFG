from collections import defaultdict

class Solution:
    def getCount(self, s: str, k: int) -> int:
        group_counts = defaultdict(int)
        n = len(s)

        if n > 0:
            group_counts[s[0]] += 1

        for i in range(1, n):
            if s[i] != s[i - 1]:
                group_counts[s[i]] += 1

        # Count how many characters appear in exactly k groups
        ans = 0
        for char, count in group_counts.items():
            if count == k:
                ans += 1

        return ans