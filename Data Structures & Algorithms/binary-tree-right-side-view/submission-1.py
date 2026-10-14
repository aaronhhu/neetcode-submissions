# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if root is None:
            return []

        q = deque()
        q.append(root)
        depth = 1

        while q:
            rightSide = None
            size = len(q)

            for i in range(size):
                cur = q.popleft()
                rightSide = cur

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)


            res.append(rightSide.val)

        return res
