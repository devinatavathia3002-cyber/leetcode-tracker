# Last updated: 2/9/2026, 9:53:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        total = 0

        def findNum(root):
            nonlocal total

            if not root:
                return (0, 0)
            
            (sumRight, countRight) = findNum(root.right)
            (sumLeft, countLeft) = findNum(root.left)
            
            theSum = sumRight + sumLeft + root.val
            numNodes = countRight + countLeft + 1

            if root.val == (theSum // numNodes):
                total += 1
            
            return (theSum, numNodes)


        findNum(root)
        return total