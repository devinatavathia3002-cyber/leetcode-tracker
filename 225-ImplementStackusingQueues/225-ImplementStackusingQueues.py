# Last updated: 2/26/2026, 10:02:21 PM
1class MyStack:
2
3    def __init__(self):
4        self.q1 = deque()
5        self.q2 = deque()
6
7    def push(self, x: int) -> None:
8        self.q2.append(x)
9        while self.q1:
10            self.q2.append(self.q1.popleft())
11        self.q1, self.q2 = self.q2, self.q1
12
13    def pop(self) -> int:
14        return self.q1.popleft()
15
16    def top(self) -> int:
17        return self.q1[0]
18
19    def empty(self) -> bool:
20        return len(self.q1) == 0