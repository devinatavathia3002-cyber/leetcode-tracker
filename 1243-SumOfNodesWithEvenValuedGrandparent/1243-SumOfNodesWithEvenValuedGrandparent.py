# Last updated: 2/9/2026, 9:54:09 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # with bfs
        """ dequeue = []
        dequeue.append([root, TreeNode(3)])

        evenTotal = 0

        while len(dequeue) > 0:
            currLen = len(dequeue)
            for i in range(currLen):
                popped = dequeue.pop(0)
                
                if popped[0].right:
                    dequeue.append([popped[0].right, popped[0]])
                    if popped[1].val % 2 == 0:
                        evenTotal += popped[0].right.val
                if popped[0].left:
                    dequeue.append([popped[0].left, popped[0]])
                    if popped[1].val % 2 == 0:
                        evenTotal += popped[0].left.val

        return evenTotal"""

        # with dfs

        def findSum(root, parent, grandparent):
            if not root:
                return 0
            
            total = 0
            if grandparent.val % 2 == 0:
                total += root.val
            
            total += findSum(root.right, root, parent)
            total += findSum(root.left, root, parent)
            
            return total
        
        return findSum(root, TreeNode(3), TreeNode(3))
                    

        