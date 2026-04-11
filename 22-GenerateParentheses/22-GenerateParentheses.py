# Last updated: 4/11/2026, 1:10:56 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        
4        stack = []
5        res = []
6
7        def backtrack(opening, close):
8            nonlocal stack
9            nonlocal res
10
11            if opening == close == n:
12                res.append("".join(stack.copy()))
13                return
14            
15            if opening < n:
16                stack.append('(')
17                backtrack(opening + 1, close)
18                stack.pop()
19            
20            if close < opening:
21                stack.append(')')
22                backtrack(opening, close + 1)
23                stack.pop()
24            
25
26        backtrack(0, 0)
27        return res