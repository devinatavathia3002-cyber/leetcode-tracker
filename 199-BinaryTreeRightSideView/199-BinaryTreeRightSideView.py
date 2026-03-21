# Last updated: 3/20/2026, 6:59:47 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        
11        if not root:
12            return []
13
14        q = deque()
15        q.append(root)
16        fin = []
17
18        while q:
19            last = -1
20            for i in range(len(q)):
21                node = q.popleft()
22
23                if node.left:
24                    q.append(node.left)
25                if node.right:
26                    q.append(node.right)
27                
28                last = node.val
29            fin.append(last)
30            
31        return fin