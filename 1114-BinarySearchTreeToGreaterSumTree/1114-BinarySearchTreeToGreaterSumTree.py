# Last updated: 2/9/2026, 9:54:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def changeVals(root, currSum):
            if not root:
                return currSum
        
            right = changeVals(root.right, currSum)
            root.val += right
            left = changeVals(root.left, root.val)

            return left
        
        originalRoot = root
        changeVals(root, 0)
        return originalRoot