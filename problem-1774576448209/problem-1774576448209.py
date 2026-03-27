# Last updated: 3/26/2026, 6:54:08 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9
10        def traverse(node):
11            if not node:
12                return 0
13            
14            return (treatAsRoot(node, 0) + traverse(node.right) + traverse(node.left))
15        
16        def treatAsRoot(node, total):
17            if not node:
18                return 0
19            
20            total += node.val
21            res = 0
22
23            if total == targetSum:
24                res += 1
25            
26            res += treatAsRoot(node.right, total)
27            res += treatAsRoot(node.left, total)
28
29            return res
30
31
32        return traverse(root)