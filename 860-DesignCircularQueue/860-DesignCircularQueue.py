# Last updated: 2/9/2026, 9:54:34 PM
class MyCircularQueue:

    def __init__(self, k: int):
        self.start = -1
        self.end = -1
        self.arr = [None] * k
        self.count = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        # can't enqueue if queue length is at max
        if self.count == self.k:
            return False
        
        # insert value at end of queue
        newIndex = (self.end + 1) % self.k
        self.arr[newIndex] = value
        self.end = newIndex
        self.count += 1
        
        # make sure to update start too if it's @ -1
        if self.start == -1:
            self.start += 1
        
        return True

    def deQueue(self) -> bool:
        # can't dequeue if there's nothing in the queue
        if self.count == 0:
            return False
        
        # remove start element
        newIndex = (self.start + 1) % self.k
        self.count -= 1
        self.start = newIndex
        
        return True
        

    def Front(self) -> int:
        # return -1 if there are no elements
        if self.count == 0:
            return -1
        
        # get and return first element
        firstElement = self.arr[self.start]
        return firstElement
        
    def Rear(self) -> int:
        # return -1 if there are no elements
        if self.count == 0:
            return -1
        
        # get and return last element
        lastElement = self.arr[self.end]
        return lastElement

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()