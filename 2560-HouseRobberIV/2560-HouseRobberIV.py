# Last updated: 7/26/2026, 3:41:53 PM
1class Solution:
2    def minCapability(self, nums: List[int], k: int) -> int:
3        
4        def possible(capability):
5            count = 0
6            i = 0
7
8            while i < (len(nums)):
9                curr = nums[i]
10                if count == k:
11                    break
12                if curr <= capability:
13                    count += 1
14                    i += 2
15                else:
16                    i += 1
17            
18            return count >= k
19        
20
21        l, r = min(nums), max(nums)
22        res = max(nums)
23
24        while l <= r:
25            mid = ((r - l) // 2) + l
26            if possible(mid):
27                res = min(res, mid)
28                r = mid - 1
29            else:
30                l = mid + 1
31        
32        return res
33