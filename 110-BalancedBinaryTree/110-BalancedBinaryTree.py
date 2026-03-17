# Last updated: 3/17/2026, 1:03:23 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isBalanced(self, root: Optional[TreeNode]) -> bool:
10        
11        flag = True
12
13        def dfs(node):
14            nonlocal flag
15            
16            if not node:
17                return 0
18            
19            left = dfs(node.left)
20            right = dfs(node.right)
21
22            # do true/false comparison here
23            if abs(left - right) > 1:
24                flag = False
25
26            return max(left, right) + 1
27
28        dfs(root) 
29        return flag