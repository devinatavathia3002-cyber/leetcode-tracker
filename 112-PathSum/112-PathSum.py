# Last updated: 3/25/2026, 5:55:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
9        
10        def hasPath(node, val):
11
12            if not node:
13                return False
14            
15            newSum = val + node.val
16            if newSum == targetSum and node.right is None and node.left is None:
17                return True
18            
19            return hasPath(node.right, val + node.val) or hasPath(node.left, val + node.val)
20        
21        if not root:
22            return False
23        return hasPath(root, 0)
24            
25            