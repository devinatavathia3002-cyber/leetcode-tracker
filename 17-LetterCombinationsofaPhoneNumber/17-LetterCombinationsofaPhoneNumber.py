# Last updated: 4/12/2026, 2:06:17 AM
1class Solution:
2    def letterCombinations(self, digits: str) -> List[str]:
3        
4        if not digits:
5            return []
6            
7        mapp = {"2" : "abc",
8                "3" : "def",
9                "4" : "ghi",
10                "5" : "jkl",
11                "6" : "mno",
12                "7" : "pqrs",
13                "8" : "tuv",
14                "9" : "wxyz"}
15
16        res = []
17
18        def dfs(index, sub):
19            nonlocal res
20
21            if len(sub) == len(digits):
22                res.append("".join(sub.copy()))
23                return
24  
25            for i in range(0, len(mapp[digits[index]])):
26                sub.append(mapp[digits[index]][i])
27                dfs(index + 1, sub)
28                sub.pop()
29        
30        dfs(0, [])
31        return res