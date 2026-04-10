# Last updated: 4/10/2026, 2:12:29 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        
4        # pass in: hashmap, index, currList
5        res = []
6        count = defaultdict(bool)
7        for num in nums:
8            count[num] = False
9
10        def backtracking(mapping, curr):
11            nonlocal res
12
13            if len(curr) == len(nums):
14                res.append(curr.copy())
15                return
16            
17            for val in nums:
18                if mapping[val] == True:
19                    continue
20                curr.append(val)
21                mapping[val] = True
22                backtracking(mapping, curr)
23                curr.pop()
24                mapping[val] = False
25        
26
27        backtracking(count, [])
28        return res
29