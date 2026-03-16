# Last updated: 3/15/2026, 5:20:53 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxDepth(self, root: Optional[TreeNode]) -> int:
10        
11        amt = 0
12
13        def maximum(node, count):
14            nonlocal amt
15            
16            if not node:
17                amt = max(amt, count)
18                return
19            
20            maximum(node.right, count + 1)
21            maximum(node.left, count + 1)
22        
23        maximum(root, 0)
24        return amt