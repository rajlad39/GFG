class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # If lengths are different, transformation is impossible
        if len(s1) != len(s2):
            return False

        n = len(s1)
        i = j = 0

        while True:
            # Skip all '#' in s1
            while i < n and s1[i] == '#':
                i += 1
            # Skip all '#' in s2
            while j < n and s2[j] == '#':
                j += 1

            # If both pointers reach the end, transformation is possible
            if i == n and j == n:
                return True

            # If one reaches the end before the other, or characters don't match
            if i == n or j == n or s1[i] != s2[j]:
                return False

            # Check movement validity
            if s1[i] == 'A' and i < j:  # 'A' cannot move right
                return False
            if s1[i] == 'B' and i > j:  # 'B' cannot move left
                return False

            i += 1
            j += 1