# Last updated: 2/9/2026, 9:54:08 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = []
        finalList = []
        queue.append(root)

        while len(queue) > 0:
            levelList = []
            levelLen = len(queue)
            for i in range(levelLen):
                currNode = queue.pop(0)
                levelList.append(currNode.val)

                if currNode.right:
                    queue.append(currNode.right)
                if currNode.left:
                    queue.append(currNode.left)
            finalList.append(levelList)
        
        leafNodes = finalList[len(finalList) - 1]
        finalSum = 0
        for i in range(len(leafNodes)):
            finalSum += leafNodes[i]
        return finalSum
            


        