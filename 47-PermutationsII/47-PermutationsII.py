# Last updated: 4/10/2026, 3:14:02 PM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        
4        count = defaultdict(int)
5        for num in nums:
6            count[num] += 1
7        res = []
8        
9        def backtracking(count, sub):
10            nonlocal res
11            if len(sub) == len(nums):
12                res.append(sub.copy())
13                return
14            
15            for val in count.keys():
16                if count[val] > 0:
17                    sub.append(val)
18                    count[val] -= 1
19                    backtracking(count, sub)
20                    sub.pop()
21                    count[val] += 1
22        
23
24        backtracking(count, [])
25        return res
26