# Last updated: 5/2/2026, 8:12:34 PM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4        if total % 2 != 0:
5            return False
6        dp = set()
7        dp.add(0)
8        target = total //2 
9
10        for num in nums:
11            newTarget = target - num
12            if newTarget in dp:
13                return True
14            
15            replica = dp.copy()
16            for val in dp:
17                replica.add(val)
18                replica.add(val + num)
19            dp = replica
20        
21        return False
22        
23        