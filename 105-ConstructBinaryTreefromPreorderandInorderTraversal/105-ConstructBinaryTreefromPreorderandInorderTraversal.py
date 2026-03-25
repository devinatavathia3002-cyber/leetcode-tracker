# Last updated: 3/25/2026, 4:47:29 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
10
11        preIndex = 0
12        indices = {val: idx for idx, val in enumerate(inorder)}
13
14        def divide(l, r):
15            nonlocal preIndex
16
17            if l > r:
18                return None
19
20            node = TreeNode(preorder[preIndex])
21            mid = indices.get(node.val)
22            preIndex += 1
23
24            node.left = divide(l, mid - 1)
25            node.right = divide(mid + 1, r)
26
27            return node
28        
29        return divide(0, len(preorder) - 1)