# Last updated: 3/23/2026, 12:14:12 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
10        
11        # in order traversal
12        top = k
13
14        def inorder(node):
15            nonlocal top
16
17            if node is None:
18                return None
19
20            left = inorder(node.left)
21            if left is not None:
22                return left
23            
24            top -= 1
25            if top == 0:
26                return node.val
27            
28            return inorder(node.right)
29        
30        return inorder(root)