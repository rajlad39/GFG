class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def pairsViolatingBST(self, root: Node) -> int:
        # Step 1: Perform inorder traversal to get node values
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)

        inorder(root)

        # Step 2: Count inversions using Merge Sort
        def merge_sort(sub_arr):
            if len(sub_arr) <= 1:
                return sub_arr, 0

            mid = len(sub_arr) // 2
            left, count_left = merge_sort(sub_arr[:mid])
            right, count_right = merge_sort(sub_arr[mid:])

            merged = []
            i = j = 0
            inv_count = count_left + count_right

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    # All remaining elements in 'left' are greater than right[j]
                    inv_count += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, total_inversions = merge_sort(arr)
        return total_inversions