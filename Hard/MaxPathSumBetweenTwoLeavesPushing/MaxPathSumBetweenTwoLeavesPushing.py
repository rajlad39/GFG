class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return float('-inf')

            # Leaf node
            if not node.left and not node.right:
                return node.data

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # If node has both left and right children, it can form a valid leaf-to-leaf path
            if node.left and node.right:
                self.max_sum = max(self.max_sum, left_sum + right_sum + node.data)
                return max(left_sum, right_sum) + node.data

            # If only left child exists
            if node.left:
                return left_sum + node.data

            # If only right child exists
            return right_sum + node.data

        dfs(root)

        # If max_sum was never updated, fewer than 2 leaf nodes existed
        return self.max_sum if self.max_sum != float('-inf') else -1