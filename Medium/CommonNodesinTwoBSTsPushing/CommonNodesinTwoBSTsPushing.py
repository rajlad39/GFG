class Solution:
    # Function to find the nodes that are common in both BSTs.
    def findCommon(self, r1, r2):
        stack1 = []
        stack2 = []
        res = []

        while True:
            # Push all left nodes of first BST
            while r1:
                stack1.append(r1)
                r1 = r1.left

            # Push all left nodes of second BST
            while r2:
                stack2.append(r2)
                r2 = r2.left

            # If either stack is empty, no more common elements are possible
            if not stack1 or not stack2:
                break

            top1 = stack1[-1]
            top2 = stack2[-1]

            # Case 1: Common node found
            if top1.data == top2.data:
                res.append(top1.data)
                stack1.pop()
                stack2.pop()
                # Move to the right subtrees
                r1 = top1.right
                r2 = top2.right

            # Case 2: First BST's current node is smaller
            elif top1.data < top2.data:
                stack1.pop()
                r1 = top1.right

            # Case 3: Second BST's current node is smaller
            else:
                stack2.pop()
                r2 = top2.right

        return res