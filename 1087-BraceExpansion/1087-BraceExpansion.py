# Last updated: 7/29/2026, 7:52:49 PM
1class Solution:
2    def expand(self, s: str) -> List[str]:
3        output = []
4        length = len(s)
5
6        def backtrack(i, curr):
7            if i >= length:
8                output.append(curr)
9                return
10            
11            char = s[i]
12            if char == "{":
13                ending = s.index("}", i)
14                options = s[i + 1:ending]
15                for option in sorted(options.split(",")):
16                    backtrack(ending + 1, curr + option)
17            else:
18                backtrack(i + 1, curr + char)
19
20        backtrack(0, "")
21        return output