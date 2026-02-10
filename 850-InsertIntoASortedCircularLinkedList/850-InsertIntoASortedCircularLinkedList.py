# Last updated: 2/9/2026, 9:54:35 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        
        new_node = Node(insertVal)
        
        if head is None:
            head = new_node
            new_node.next = new_node
            return head
        
        # main case
        
        curr = head.next
        prev = head
        
        while True:
            # case 1, insert between two nodes
            if prev.val <= insertVal <= curr.val:
                break
            
            # check at turning point (max --> min)
            if prev.val > curr.val:
                if insertVal <= curr.val or insertVal >= prev.val:
                    break
            
            # insert anywhere if all values are the same
            if curr == head:
                break
            
            prev = curr
            curr = curr.next
                
                
        prev.next = new_node
        new_node.next = curr
        return head