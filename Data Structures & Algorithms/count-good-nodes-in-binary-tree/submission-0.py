# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(curr, maximum):
            if curr is None:
                return

            if curr.val >= maximum:
                self.res += 1
                maximum = curr.val

            dfs(curr.left, maximum)
            dfs(curr.right, maximum)

        dfs(root, root.val)

        return self.res
