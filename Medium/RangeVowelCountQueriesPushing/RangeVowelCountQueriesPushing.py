class Solution:
    def countVowels(self, s: str, queries: list[list[int]]) -> list[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)
        pref = [0] * (n + 1)

        for i, ch in enumerate(s):
            pref[i + 1] = pref[i] + (1 if ch in vowels else 0)

        ans = []
        for l, r in queries:
            ans.append(pref[r + 1] - pref[l])

        return ans
        