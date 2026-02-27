# Last updated: 2/26/2026, 10:42:30 PM
1class MyQueue:
2
3    def __init__(self):
4        self.s1 = []
5        self.s2 = []
6
7    def push(self, x: int) -> None:
8        while self.s1:
9            self.s2.append(self.s1.pop())
10        self.s1.append(x)
11        while self.s2:
12            self.s1.append(self.s2.pop())
13
14    def pop(self) -> int:
15        return self.s1.pop()
16
17    def peek(self) -> int:
18        return self.s1[-1]
19
20    def empty(self) -> bool:
21        return len(self.s1) == 0