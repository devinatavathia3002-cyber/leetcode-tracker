# Last updated: 5/31/2026, 2:40:58 PM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        # without fast/slow pointers
4        # seen = []
5        # newVal = n
6
7        # while newVal not in seen and newVal != 1:
8        #     nextVal = 0
9        #     seen.append(newVal)
10        #     while newVal > 0:
11        #         last = newVal % 10
12        #         newVal = newVal // 10
13
14        #         nextVal += (last * last) 
15        #     newVal = nextVal
16        
17        # if newVal == 1:
18        #     return True
19        # return False
20
21        # with cycle detection (floyd's)
22        slow = n
23        fast = self.sumOfSquares(slow)
24
25        while slow != fast and slow != 1:
26            slow = self.sumOfSquares(slow)
27            fast = self.sumOfSquares(self.sumOfSquares(fast))
28        if slow == 1:
29            return True
30        return False
31
32    def sumOfSquares(self, val):
33        nextVal = 0
34        while val > 0:
35            last = val % 10
36            val = val // 10
37
38            nextVal += (last * last) 
39        return nextVal