# Last updated: 2/9/2026, 9:54:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        tracker = root
        
        while tracker:
            
            if tracker.val < val and tracker.right is None:
                tracker.right = TreeNode(val)
                return root
            
            elif tracker.val > val and tracker.left is None:
                tracker.left = TreeNode(val)
                return root 
            
            elif tracker.val < val:
                tracker = tracker.right
            
            else:
                tracker = tracker.left
        
        root = TreeNode(val)
        return root 