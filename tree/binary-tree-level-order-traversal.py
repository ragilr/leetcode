# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bsf(root):
            ret = []
            if not root:
                return ret
            q = deque()
            q.append(root)
            while q:
                l = len(q)
                ret.append([])
                for i in range(l):
                    node = q.popleft()
                    ret[-1].append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            return ret
        
        return bsf(root)