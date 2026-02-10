# Last updated: 2/9/2026, 9:54:23 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def findSum(root, low, high):
            total = 0

            if not root:
                return 0
            
            if root.val >= low and root.val <= high:
                total += root.val
            
            total += findSum(root.right, low, high)
            total += findSum(root.left, low, high)

            return total
        
        return findSum(root, low, high)

        