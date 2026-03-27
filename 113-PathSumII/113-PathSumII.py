# Last updated: 3/26/2026, 5:42:50 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
9        
10        fin = []
11
12        def traverse(node, curr, total):
13
14            if not node:
15                return
16            
17            total += node.val
18            curr.append(node.val)
19
20            if total == targetSum and node.right is None and node.left is None:
21                fin.append(curr.copy())
22            
23            traverse(node.right, curr, total)
24            traverse(node.left, curr, total)
25
26            curr.pop()
27
28        traverse(root, [], 0)
29        return fin