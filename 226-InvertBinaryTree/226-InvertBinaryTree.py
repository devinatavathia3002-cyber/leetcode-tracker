# Last updated: 3/15/2026, 5:12:07 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
10
11        def invert(node):
12
13            if not node:
14                return
15            
16            node.right, node.left = node.left, node.right
17
18            invert(node.right)
19            invert(node.left)
20        
21        invert(root)
22        return root