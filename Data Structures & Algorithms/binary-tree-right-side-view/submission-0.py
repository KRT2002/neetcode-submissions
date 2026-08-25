# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            last = None
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    last = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if last:
                res.append(last)
        return res