# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = deque()
        node = root
        while node:
            self.stack.append(node)
            node = node.left
        # self.printStack()
    
        

    def next(self) -> int:
        ret = self.stack.pop()
        node = ret
        if node:
            node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        # self.printStack()
        return ret.val
        

    def hasNext(self) -> bool:
        return self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()