# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        sums = []
        def dfs(node):
            if node is None:
                return 0
            subtree_sum = dfs(node.left) + dfs(node.right) + node.val
            sums.append(subtree_sum)
            return subtree_sum
        m = 0
        total = dfs(root)
        for i in sums:
            prod = i*(total-i)
            if prod > m :
                m = prod
        return m % (10**9 +7)
