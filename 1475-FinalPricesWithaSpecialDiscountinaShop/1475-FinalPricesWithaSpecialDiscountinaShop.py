# Last updated: 7/16/2026, 5:07:56 PM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        stack = []
4
5        for i in range(len(prices) - 1, - 1, -1):
6            curr = prices[i]
7            while stack and stack[-1] > curr:
8                stack.pop()
9            if stack and stack[-1] <= curr:
10                prices[i] -= stack[-1]
11            stack.append(curr)
12        
13        return prices
14            