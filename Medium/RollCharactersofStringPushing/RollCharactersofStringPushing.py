class Solution:
    def findRollOut(self, s: str, roll: list[int]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        # Step 1: Record range updates using difference array
        for r in roll:
            diff[0] += 1
            if r < n:
                diff[r] -= 1

        # Step 2: Compute prefix sum to get actual increments for each index
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Step 3: Apply the total shifts cyclically to the string
        s_list = list(s)
        for i in range(n):
            if diff[i] > 0:
                original_idx = ord(s_list[i]) - ord('a')
                new_idx = (original_idx + diff[i]) % 26
                s_list[i] = chr(ord('a') + new_idx)

        return "".join(s_list)