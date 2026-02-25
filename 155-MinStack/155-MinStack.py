# Last updated: 2/25/2026, 1:03:02 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minStack = []
6
7    def push(self, val: int) -> None:
8        self.stack.append(val)
9
10        if len(self.minStack) == 0:
11            self.minStack.append(val)
12        else:
13            self.minStack.append(min(self.minStack[-1], val))
14
15    def pop(self) -> None:
16        self.stack.pop()
17        self.minStack.pop()
18
19    def top(self) -> int:
20        return self.stack[-1]
21        
22    def getMin(self) -> int:
23        return self.minStack[-1]
24