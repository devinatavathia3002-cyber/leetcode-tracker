# Last updated: 6/8/2026, 8:31:50 PM
1class Solution:
2    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
3        
4        output = []
5
6        def backtrack(total, sub, i):
7            if total > target:
8                return 
9            elif total == target:
10                output.append(sub.copy())
11            else:
12                for j in range(i, len(nums)):
13                    sub.append(nums[j])
14                    backtrack(total + nums[j], sub, j)
15                    sub.pop()
16            
17        backtrack(0, [], 0)
18        return output
19