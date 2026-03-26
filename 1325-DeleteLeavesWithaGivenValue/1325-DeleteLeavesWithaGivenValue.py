# Last updated: 3/25/2026, 5:32:19 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
9        
10        def delLeaves(node):
11
12            if not node:
13                return None
14            
15            node.right = delLeaves(node.right)
16            node.left = delLeaves(node.left)
17
18            if node.val == target and node.right is None and node.left is None:
19                return None
20
21            return node
22        
23        return delLeaves(root)