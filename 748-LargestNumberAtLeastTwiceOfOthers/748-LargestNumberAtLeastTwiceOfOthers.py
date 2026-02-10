# Last updated: 2/9/2026, 9:54:52 PM
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        index = 0
        for i in range(len(nums)):
            largest = max(nums[index], nums[i])
            if largest != nums[index]:
                index = i
        
        boundary = (nums[index]) // 2
        
        for num in nums:
            if num > boundary and num != nums[index]:
                return -1
        
        return index
        