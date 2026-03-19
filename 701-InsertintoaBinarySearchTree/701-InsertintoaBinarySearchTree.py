# Last updated: 3/18/2026, 10:49:38 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
9        
10        if root is None:
11            root = TreeNode(val)
12            return root
13            
14        pointer = root
15
16        while True:
17            if pointer.right is None and pointer.val < val:
18                pointer.right = TreeNode(val)
19                break
20            elif pointer.left is None and pointer.val > val:
21                pointer.left = TreeNode(val)
22                break
23            elif pointer.val < val:
24                pointer = pointer.right
25            else:
26                pointer = pointer.left
27
28        return root