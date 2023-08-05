# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def bsf(root):
            if not root:
                return []
            visited = set()
            q=deque()
            q.append([root,0])
            ret=[]
            while q:
                v = q.popleft()
                node = v[0]
                level = v[1]
                visited.add(node)
                if len(ret)==level:
                    # print("here")
                    ret.append([])
                # print(ret)
                ret[level].append(node.val)
                if node.left and node.left not in visited:
                    q.append([node.left,level+1])
                if node.right and node.right not in visited:
                    q.append([node.right,level+1])
            return ret
        
        return bsf(root)
                
        