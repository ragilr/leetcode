# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        mem = dict()
        def makeRoot(n):
            # print("makeRoot",n)
            if n == 1:
                return [TreeNode()]
            if n == 0:
                return None
            if n in mem:
                return mem[n]
            ret = []
            for i in range(1,n-1,2):
                for left in  makeRoot(i):
                    for right in makeRoot(n-i-1):
                        ret.append(TreeNode(0,left,right))
            mem[n]=ret
            return ret
        x=makeRoot(n)
        return x
