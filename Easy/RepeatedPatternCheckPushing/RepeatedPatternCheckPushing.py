class Solution:
    def findPattern(self, s: str) -> bool:
        i = 0
        n = len(s)

        while i < n:
            # Count consecutive 'x's
            count_x = 0
            while i < n and s[i] == 'x':
                count_x += 1
                i += 1

            # Count consecutive 'y's
            count_y = 0
            while i < n and s[i] == 'y':
                count_y += 1
                i += 1

            # The number of 'x's and 'y's must be equal for this segment
            if count_x == 0 or count_x != count_y:
                return False

        return True