# Last updated: 2/26/2026, 10:04:26 PM
1class MyStack:
2
3    def __init__(self):
4        self.q1 = deque()
5
6    def push(self, x: int) -> None:
7        old = len(self.q1)
8        self.q1.append(x)
9        for i in range(old):
10            self.q1.append(self.q1.popleft())
11
12    def pop(self) -> int:
13        return self.q1.popleft()
14
15    def top(self) -> int:
16        return self.q1[0]
17
18    def empty(self) -> bool:
19        return len(self.q1) == 0