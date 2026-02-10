# Last updated: 2/9/2026, 9:54:35 PM
class ListNode:
    
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return - 1
        tracker = 0
        curr = self.head
        while tracker != index:
            tracker += 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        
        new_node.next = self.head
        self.head.prev = new_node        
        self.head = new_node
        
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            self.size += 1
            return
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
        self.size += 1
            

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == (self.size):
            self.addAtTail(val)
            return
        
        new_node = ListNode(val)
        temp = self.head
        tracker = 0
        
        while tracker < index - 1:
            temp = temp.next
            tracker += 1
            
        new_node.next = temp.next
        new_node.prev = temp
        
        temp.next = new_node
        if new_node.next.prev:
            new_node.next.prev = new_node
        
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        if index == 0:                
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return
        
        temp = self.head
        tracker = 0
        while tracker < index - 1:
            temp = temp.next
            tracker += 1
        
        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp
        
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)