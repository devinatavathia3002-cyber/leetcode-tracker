# Last updated: 3/20/2026, 6:07:42 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        
11        ans = root
12
13        def LCA(node, p, q):
14            nonlocal ans
15
16            if not node:
17                return False
18            
19            mid = (node.val == p.val or node.val == q.val)
20
21            left = LCA(node.left, p, q)
22            right = LCA(node.right, p, q)
23
24            if mid + left + right >= 2:
25                ans = node
26            
27            return mid or left or right
28
29        LCA(root, p, q)
30        return ans
31        