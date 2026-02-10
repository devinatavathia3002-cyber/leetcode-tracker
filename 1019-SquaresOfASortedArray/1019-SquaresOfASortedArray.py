# Last updated: 2/9/2026, 9:54:22 PM
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        beg = 0
        end = len(nums) - 1
        
        res = [0] * len(nums)
        resPointer = len(nums) - 1
        
        while beg <= end:
            num1 = abs(nums[beg])
            num2 = abs(nums[end])
            
            if num1 >= num2:
                res[resPointer] = num1 * num1
                beg += 1
            else:
                res[resPointer] = num2 * num2
                end -= 1
            
            resPointer -= 1
            
        return res
            
                
        