# Last updated: 2/9/2026, 9:54:00 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        output = 0
        maxVal = float('-inf')
        if not root:
            return output
        
        def findGoodNodes(root, maxVal):
            output = 0

            if not root:
                return output

            maxVal = max(maxVal, root.val)
            if (maxVal == root.val):
                output += 1

            r = findGoodNodes(root.right, maxVal) 
            l = findGoodNodes(root.left, maxVal)

            return r + l + output
        
        return findGoodNodes(root, maxVal)
            

        