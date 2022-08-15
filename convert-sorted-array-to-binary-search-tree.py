# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makebst(l,h):
            if l>h:
                return None
            mid = (l+h)//2
            left=makebst(l,mid-1)
            right=makebst(mid+1,h)
            node = TreeNode(nums[mid],left,right)
            return node
        return makebst(0,len(nums)-1)
        