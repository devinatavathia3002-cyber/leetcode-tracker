# Last updated: 3/15/2026, 3:54:11 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        result = []
11
12        def postorder(node):
13
14            if not node:
15                return
16            
17            postorder(node.left)
18            postorder(node.right)
19            result.append(node.val)
20
21        
22        postorder(root)
23        return result
24
25
26
27