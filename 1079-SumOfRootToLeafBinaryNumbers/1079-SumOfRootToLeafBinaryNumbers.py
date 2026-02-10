# Last updated: 2/9/2026, 9:54:17 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def sumLeftLeaf(root, sumVal):
            totalSum = 0

            if not root:
                return 0

            if root.right is None and root.left is None:
                totalSum += (int(str(sumVal * 10 + root.val), 2))

            totalSum += sumLeftLeaf(root.right, sumVal * 10 + root.val)
            totalSum += sumLeftLeaf(root.left, sumVal * 10 + root.val)

            return totalSum

        
        return sumLeftLeaf(root, 0)


        