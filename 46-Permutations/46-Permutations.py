# Last updated: 6/15/2026, 8:56:32 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        
4        output = []
5        mapping = defaultdict(bool)
6        for num in nums:
7            mapping[num] = False
8        
9        def backtrack(sub):
10            if len(sub) == len(nums):
11                output.append(sub)
12                return
13            
14            for num in nums:
15                if mapping[num]:
16                    continue
17                sub.append(num)
18                mapping[num] = True
19                backtrack(sub.copy())
20                mapping[num] = False
21                sub.pop()
22
23
24        backtrack([])
25        return output