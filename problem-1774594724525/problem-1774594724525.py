# Last updated: 3/26/2026, 11:58:44 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
9        
10        pathSum = {0: 1}
11
12        def findPaths(node, total):
13
14            if node is None:
15                return 0
16            
17            total += node.val
18            res = pathSum.get(total - targetSum, 0)
19
20            pathSum[total] = pathSum.get(total, 0) + 1
21
22            res += findPaths(node.right, total)
23            res += findPaths(node.left, total)
24
25            # backtrack
26            pathSum[total] -= 1
27
28            return res
29        
30        return findPaths(root, 0)