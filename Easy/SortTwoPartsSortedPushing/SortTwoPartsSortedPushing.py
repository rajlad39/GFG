class Solution:
    def mergeTwoParts(self, arr: list[int]) -> None:
        n = len(arr)
        if n <= 1:
            return

        # Find the break point
        index = 0
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                index = i + 1
                break

        # If no break point found, it's already sorted
        if index == 0:
            return

        # Two pointers for merging
        i = 0
        j = index
        temp = []

        while i < index and j < n:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i < index:
            temp.append(arr[i])
            i += 1

        while j < n:
            temp.append(arr[j])
            j += 1

        # Copy back to original array
        for x in range(n):
            arr[x] = temp[x]