from typing import List

class Solution:
    def generateUsernames(self, arr: List[str]) -> List[str]:
        counts = {}
        ans = []
        used = set()
        reserved = set(arr)

        for name in arr:
            if name not in used:
                ans.append(name)
                used.add(name)
                counts[name] = 1
            else:
                k = counts.get(name, 1)
                candidate = f"{name}{k}"
                while candidate in used or candidate in reserved:
                    k += 1
                    candidate = f"{name}{k}"
                counts[name] = k + 1
                ans.append(candidate)
                used.add(candidate)

        return ans