# Last updated: 4/12/2026, 1:35:58 AM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        
4        res = []
5        pal = []
6
7        def dfs(index):
8            nonlocal res
9
10            if index == len(s):
11                res.append(pal.copy())
12                return
13            
14            for i in range(index, len(s)):
15                if isPalindrome(s, index, i):
16                    pal.append(s[index : i + 1])
17                    dfs(i + 1)
18                    pal.pop()
19
20
21        def isPalindrome(s, l, r):
22            while l < r:
23                if s[l] != s[r]:
24                    return False
25                l += 1
26                r -= 1
27            return True
28        
29        dfs(0)
30        return res