# Last updated: 6/15/2026, 11:06:40 PM
1class Solution:
2    def mostPoints(self, questions: List[List[int]]) -> int:
3        
4        # with recursion
5        # def backtrack(i):
6        #     if i >= len(questions):
7        #         return 0
8        #     pts, skip = questions[i]
9
10        #     choose = pts + backtrack(i + skip + 1)
11        #     notChoose = backtrack(i + 1)
12
13        #     return max(choose, notChoose)
14        
15        # return backtrack(0)
16
17        # with dp array
18        dp = [0] * len(questions)
19        dp[len(questions) - 1] = questions[len(questions) - 1][0]
20
21        for i in range(len(questions) - 2, -1, -1):
22            pts, skip = questions[i]
23            skip = i + skip + 1
24
25            choose = (pts + dp[skip]) if skip < len(questions) else pts
26            notChoose = dp[i + 1]
27
28            dp[i] = max(choose, notChoose)
29        
30        return dp[0]
31        