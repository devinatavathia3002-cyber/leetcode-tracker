# Last updated: 3/5/2026, 8:07:40 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        
4        l = 0
5        r = 0
6
7        q = set()
8
9        while r < len(nums):
10
11            if (r - l) > k:
12                q.remove(nums[l])
13                l += 1
14            
15            if nums[r] in q:
16                return True
17            
18            q.add(nums[r])
19
20            r += 1
21        
22        return False