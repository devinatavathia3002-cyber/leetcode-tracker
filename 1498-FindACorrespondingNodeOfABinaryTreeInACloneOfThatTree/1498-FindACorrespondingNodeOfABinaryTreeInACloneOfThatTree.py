# Last updated: 2/9/2026, 9:54:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        reference = None

        def findCopy(root):
            nonlocal reference

            if not root:
                return
        
            if root.val == target.val:
                reference = root
            
            findCopy(root.right)
            findCopy(root.left)
        
        findCopy(cloned)
        return reference
            


        

        