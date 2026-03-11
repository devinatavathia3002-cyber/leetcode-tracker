# Last updated: 3/10/2026, 9:17:47 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3
4        for i in range(len(nums)):
5            index = abs(nums[i])
6            if nums[index] < 0:
7                return index
8
9            nums[index] = -1 * nums[index]