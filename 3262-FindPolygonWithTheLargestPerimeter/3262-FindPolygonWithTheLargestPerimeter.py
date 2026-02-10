# Last updated: 2/9/2026, 9:53:51 PM
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        list.sort(nums)
        n = len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        i = n - 1
        while i >= 0:
            sum = sum - nums[i]
            if nums[i] < sum:
                return sum + nums[i]
            i -= 1
        return -1
        