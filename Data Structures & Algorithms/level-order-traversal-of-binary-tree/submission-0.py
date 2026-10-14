# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return []

        q = deque()
        q.append(root)
        depth = 1

        while q:
            size = len(q)
            res.append([])
            for i in range(size):
                cur = q.popleft()
                res[depth-1].append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            depth += 1


        return res