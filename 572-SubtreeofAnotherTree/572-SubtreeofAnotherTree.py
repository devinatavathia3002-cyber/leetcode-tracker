# Last updated: 3/18/2026, 4:42:27 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:   
9    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
10
11        def compare(node, subRoot):
12            if not node:
13                return False
14
15            if node:
16                if node.val == subRoot.val:
17                    if isSame(node, subRoot):
18                        return True
19            return compare(node.right, subRoot) or compare(node.left, subRoot)
20
21        def isSame(p1, p2):
22            if p1 is None and p2 is None:
23                return True
24            if p1 is None:
25                return False
26            if p2 is None:
27                return False
28            
29            if p1.val != p2.val:
30                return False
31            
32            return isSame(p1.right, p2.right) and isSame(p1.left, p2.left)
33        
34        return compare(root, subRoot)