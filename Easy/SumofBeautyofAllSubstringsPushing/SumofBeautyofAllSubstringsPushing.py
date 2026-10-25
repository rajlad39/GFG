class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0

        for i in range(n):
            freq = {}
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1

                max_f = max(freq.values())
                min_f = min(freq.values())

                total_beauty += (max_f - min_f)

        return total_beauty