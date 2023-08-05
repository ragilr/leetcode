# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,inorder):
            # print(preorder,inorder)
            if len(preorder)==0 or len(inorder)==0:
                return None
            n = preorder[0]
            node = TreeNode()
            node.val = n
            index = inorder.index(n)
            leftInorder = inorder[:index]
            rightInorder = inorder[index+1:]
            build.preorder = build.preorder[1:]
            node.left = build(build.preorder,leftInorder)
            node.right = build(build.preorder,rightInorder)
            return node
        build.preorder = preorder
        return build(build.preorder,inorder)