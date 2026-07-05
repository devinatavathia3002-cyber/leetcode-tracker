# Last updated: 7/4/2026, 8:59:39 PM
1class Solution:
2    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
3        total = sum(nums)
4        subTotal = total // k
5
6        if total % k != 0:
7            return False
8
9        nums.sort(reverse=True)
10        buckets = [0] * k
11
12        def backtrack(i):
13            if i == len(nums):
14                return True
15            
16            seen = set()
17            for j in range(k):
18                if buckets[j] + nums[i] <= subTotal and buckets[j] not in seen:
19                    seen.add(buckets[j])
20                    buckets[j] += nums[i]
21                    if backtrack(i + 1):
22                        return True
23                    buckets[j] -= nums[i]
24            
25            return False
26
27        return backtrack(0)