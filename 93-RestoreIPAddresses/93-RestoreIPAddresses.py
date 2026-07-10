# Last updated: 7/9/2026, 9:08:32 PM
1class Solution:
2    def restoreIpAddresses(self, s: str) -> List[str]:
3        output = []
4
5        def putPeriods(dots, i, sub):
6            if dots == 4 and i == len(s):
7                output.append(sub[:-1])
8                return
9            if dots > 4:
10                return
11            if i > len(s):
12                return
13            
14            for j in range(i, min(len(s), i + 3)):
15                curr = s[i:j + 1]
16                if 0 <= int(curr) <= 255:
17                    if j > i and s[i] == "0":
18                        break
19                    else:
20                        putPeriods(dots + 1, j + 1, sub + curr + ".")
21
22                else:
23                    continue
24        
25        putPeriods(0, 0, "")
26
27        return output