# Last updated: 2/9/2026, 9:54:51 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        # edge case check
        if root is None:
            return None
        
        res = []
        
        queue = deque()
        queue.append(root)
        
        # directed & acyclic so we don't need a visited array
        
        while queue:
            currLevel = []
            length = len(queue)
            
            for i in range(length):
                node = queue.popleft()
                currLevel.append(node.val)
                
                for j in node.children:
                    queue.append(j)
            
            res.append(currLevel)
        
        return res
                