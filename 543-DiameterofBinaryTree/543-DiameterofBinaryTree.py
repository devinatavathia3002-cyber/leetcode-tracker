# Last updated: 3/17/2026, 12:38:49 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
10        res = 0
11
12        def find(node):
13            nonlocal res
14
15            if not node:
16                return 0
17            
18            left = find(node.left)
19            right = find(node.right)
20            
21            res = max(res, left + right)
22
23            return 1 + max(left, right)
24        
25        find(root)
26        return res
27