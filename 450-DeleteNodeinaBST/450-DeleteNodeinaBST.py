# Last updated: 3/20/2026, 5:20:45 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
9        
10        pointer = TreeNode(-1)
11        pointer.right = root
12
13        def traverse(node, key):
14            if not node:
15                return None
16            
17            if node.val == key:
18                if node.right is None and node.left is None:
19                    return None
20            
21                elif not node.right:
22                    return node.left
23                
24                elif not node.left:
25                    return node.right
26                
27                else:
28                    curr = node
29                    curr = curr.right
30                    while curr.left:
31                        curr = curr.left
32                        
33                    node.val, curr.val = curr.val, node.val
34
35            node.right = traverse(node.right, key)
36            node.left = traverse(node.left, key)
37
38            return node
39
40        traverse(pointer, key)
41        return pointer.right