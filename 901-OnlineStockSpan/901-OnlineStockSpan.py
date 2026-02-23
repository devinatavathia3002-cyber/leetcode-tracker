# Last updated: 2/22/2026, 11:15:35 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        answer = 1
8
9        while self.stack and self.stack[-1][0] <= price:
10            [money, days] = self.stack.pop()
11            answer += days
12        
13        self.stack.append([price, answer])
14        return answer
15
16
17# Your StockSpanner object will be instantiated and called as such:
18# obj = StockSpanner()
19# param_1 = obj.next(price)