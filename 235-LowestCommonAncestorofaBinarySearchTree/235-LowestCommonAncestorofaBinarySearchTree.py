# Last updated: 3/18/2026, 9:25:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
10        
11        pointer = root
12
13        while True:
14            if p.val > pointer.val and q.val > pointer.val:
15                pointer = pointer.right
16            elif p.val < pointer.val and q.val < pointer.val:
17                pointer = pointer.left
18            else:
19                break
20        
21        return pointer