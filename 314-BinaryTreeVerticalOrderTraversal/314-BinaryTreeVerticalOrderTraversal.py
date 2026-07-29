# Last updated: 7/28/2026, 10:44:25 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        col = defaultdict(list)
10        q = deque()
11        q.append((root, 0))
12
13        if not root:
14            return []
15
16        while q:
17            node, num = q.popleft()
18            col[num].append(node.val)
19            if node.left:
20                q.append((node.left, num - 1))
21            if node.right:
22                q.append((node.right, num + 1))
23        
24        output = []
25        for key, val in sorted(col.items()):
26            output.append(val)
27        return output
28