# Last updated: 7/30/2026, 9:28:38 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root):
9        nodes = []
10        
11        def preorder(node):
12            if not node:
13                return
14            nodes.append(node)
15            preorder(node.left)
16            preorder(node.right)
17        
18        preorder(root)
19        for i in range(len(nodes) - 1):
20            nodes[i].left = None
21            nodes[i].right = nodes[i + 1]