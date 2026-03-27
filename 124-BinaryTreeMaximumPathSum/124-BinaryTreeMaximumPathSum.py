# Last updated: 3/27/2026, 12:44:44 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxPathSum(self, root: Optional[TreeNode]) -> int:
10        
11        maximum = -1000
12
13        def findPaths(node):
14            nonlocal maximum
15
16            if not node:
17                return 0
18
19            right = max(findPaths(node.right), 0)
20            left = max(findPaths(node.left), 0)
21
22            maximum = max(maximum, left + right + node.val)
23
24            return max(right, left) + node.val
25
26        findPaths(root)
27        return maximum