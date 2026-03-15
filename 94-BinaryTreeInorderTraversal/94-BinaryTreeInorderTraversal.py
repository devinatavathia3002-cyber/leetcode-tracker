# Last updated: 3/15/2026, 3:38:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
9        
10        result = []
11
12        def inorder(node):
13
14            if node is None:
15                return False
16            
17            inorder(node.left)
18            result.append(node.val)
19            inorder(node.right)
20
21        inorder(root)
22        return result