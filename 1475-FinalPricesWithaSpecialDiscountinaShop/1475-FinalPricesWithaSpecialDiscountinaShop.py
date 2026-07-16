# Last updated: 7/16/2026, 4:58:17 PM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        stack = []
4
5        for i in range(len(prices) - 1, - 1, -1):
6            curr = prices[i]
7            if len(stack) == 0:
8                stack.append(curr)
9            else:
10                while stack and stack[-1] > curr:
11                    stack.pop()
12                if stack and stack[-1] <= curr:
13                    prices[i] -= stack[-1]
14            stack.append(curr)
15        
16        return prices
17            