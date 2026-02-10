# Last updated: 2/9/2026, 9:54:46 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        iterator = root
        
        while iterator:
            if iterator.val == val:
                return iterator
            elif iterator.val < val:
                iterator = iterator.right
            else:
                iterator = iterator.left
        
        return None