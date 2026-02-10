# Last updated: 2/9/2026, 9:54:50 PM
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        def findConnections(curr):
            prev = None
            while curr:
                if curr.child:
                    tempNext = curr.next
                    childHead = curr.child

                    # Connect curr to child
                    curr.next = childHead
                    childHead.prev = curr
                    curr.child = None

                    # Flatten child and get tail
                    tail = findConnections(childHead)

                    # Connect tail to tempNext
                    if tempNext:
                        tail.next = tempNext
                        tempNext.prev = tail
                    prev = tail
                    curr = tempNext
                else:
                    prev = curr
                    curr = curr.next
            return prev  # prev is the tail of the flattened part

        findConnections(head)
        return head
