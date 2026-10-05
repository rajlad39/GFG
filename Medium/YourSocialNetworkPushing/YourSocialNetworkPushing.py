class Solution:
    def socialNetwork(self, arr: list[int]) -> list[list[int]]:
        n = len(arr) + 1  # Total number of users from 1 to n
        result = []

        # Process each user i from 2 to n
        for i in range(2, n + 1):
            reachable = []
            curr = arr[i - 2]  # Direct friend of user i
            k = 1              # Number of links followed

            # Trace all reachable users from i
            while curr > 0:
                reachable.append((curr, k))
                # Move to the friend of 'curr'
                if curr >= 2:
                    curr = arr[curr - 2]
                    k += 1
                else:
                    break

            # Sort j in increasing order (1 to i - 1)
            reachable.sort(key=lambda x: x[0])

            # Add [i, j, k] to the final result
            for j, k_val in reachable:
                result.append([i, j, k_val])

        return result