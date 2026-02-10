# Last updated: 2/9/2026, 9:54:25 PM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        i = 0
        j = 0
        
        for j in range(len(nums)):
            
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        
        return nums