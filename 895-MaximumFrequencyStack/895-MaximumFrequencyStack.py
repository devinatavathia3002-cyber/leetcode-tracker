# Last updated: 7/19/2026, 8:07:55 PM
1class FreqStack:
2
3    def __init__(self):
4        self.maxVal = 0
5        self.freq = {} # maps num to freq
6        self.stacks = {} # maps freq to list of nums (stack)
7
8    def push(self, val: int) -> None:
9        if val in self.freq:
10            self.freq[val] += 1
11        else:
12            self.freq[val] = 1
13        if self.freq[val] > self.maxVal:
14            self.maxVal = self.freq[val]
15            self.stacks[self.maxVal] = []
16        self.stacks[self.freq[val]].append(val)
17
18    def pop(self) -> int:
19        res = self.stacks[self.maxVal].pop()
20        self.freq[res] -= 1
21        if self.stacks[self.maxVal] == []:
22            self.maxVal -= 1
23        return res
24
25
26# Your FreqStack object will be instantiated and called as such:
27# obj = FreqStack()
28# obj.push(val)
29# param_2 = obj.pop()